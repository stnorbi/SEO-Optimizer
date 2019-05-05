from PyQt4.QtCore import QObject, pyqtSignal
from queue import Queue
import json, os
from threading import Thread

from googleads import adwords

google_yaml = os.path.dirname(__file__).replace('utils', 'Authentication') + "/"
# Initialize the AdWords client.
adwords_client = adwords.AdWordsClient.LoadFromStorage(google_yaml + "googleads.yaml")
targeting_idea_service = adwords_client.GetService('TargetingIdeaService', version='v201809')


dataFolder=os.path.dirname(__file__).replace('utils','Data')+'/'

if  not os.path.isdir(dataFolder):
    os.mkdir(dataFolder)


class GetStats(QObject):
    downloadFinished=pyqtSignal()

    def __init__(self):
        GetStats.__init__(self)
        self.keywordQueue=Queue()
        self.keywords=[]
        self.progress=True
        self.currentDownloaded=None

    def setKeywords(self,wordObject):
        self.keywords=wordObject

        for obj in self.keywords:
            self.keywordQueue.put(obj)

        self.getData()

    def getData(self):
        t = Thread(target=getInfoWorker, args=(self.keywordQueue, self.downloadFinished))

def getInfoWorker(queue,signal):

    while not queue.empty:
        wordObj=queue.get()

        wordData=getWordData(wordObj)

        queue.task_done()
        signal.emit()

def getWordData(keyWord):
    dataDict={}

    selector = {
        'ideaType': 'KEYWORD',
        'requestType': 'STATS',
    }

    selector['requestedAttributeTypes'] = [
        'KEYWORD_TEXT', 'SEARCH_VOLUME', 'COMPETITION', 'AVERAGE_CPC', 'TARGETED_MONTHLY_SEARCHES']

    offset = 0
    PAGE_SIZE = 100
    selector['paging'] = {
        'startIndex': str(offset),
        'numberResults': str(PAGE_SIZE)
    }

    selector['searchParameters'] = [{
        'xsi_type': 'RelatedToQuerySearchParameter',
        'queries': [keyWord]}
        , {'xsi_type': 'LocationSearchParameter', 'locations': {'id': 20415}}
        , {'xsi_type': 'LanguageSearchParameter', 'languages': {'id': 1024}}
    ]
    # időkeret felállításának nézz utánaSS

    page = targeting_idea_service.get(selector)

    for result in page['entries']:
        attributes = {}
        for attribute in result['data']:
            attributes[attribute['key']] = getattr(
                attribute['value'], 'value', '0')

        dataDict['KeyWord']=attributes['KEYWORD_TEXT'],
        dataDict['Search Volume'] =attributes['SEARCH_VOLUME'],
        dataDict['CMP'] =attributes['COMPETITION'],
        dataDict['CPC'] =attributes['AVERAGE_CPC']['microAmount'] / 1000000,
 #       dataDict['Monthly Research'] = attributes[    'TARGETED_MONTHLY_SEARCHES']

        # print('Keyword: "%s" \n average monthly search volume '
        #       '"%s" \n Competition: %s \n Average CPC: %s \n Monthly Average Search: %s' % (attributes['KEYWORD_TEXT'],
        #                                                                                     attributes['SEARCH_VOLUME'],
        #                                                                                     attributes['COMPETITION'],
        #                                                                                     attributes['AVERAGE_CPC'][
        #                                                                                         'microAmount'] / 1000000,
        #                                                                                     attributes['TARGETED_MONTHLY_SEARCHES']))
    return dataDict

def saveData(data, keyWord):
    print("saving data for", keyWord)

    with open(dataFolder + keyWord + "_data_.json", "w") as dataFile:
        json.dump(data, dataFile)


# if __name__ == "__main__":
#     for i in ['kutya','macska','véreb']:
#         getWordData(i)