from PyQt5.QtCore import QObject, pyqtSignal
from queue import Queue
import json, os,time
from threading import Thread
import pandas as pd
from zeep import Client

from googleads import adwords

google_yaml = os.path.dirname(__file__).replace('utils', 'Authentication') + "/"
# Initialize the AdWords client.
adwords_client = adwords.AdWordsClient.LoadFromStorage(google_yaml + "googleads.yaml")
targeting_idea_service = adwords_client.GetService('TargetingIdeaService', version='v201809')


dataFolder=os.path.dirname(__file__).replace('utils','Data')+'/'


if  not os.path.isdir(dataFolder):
    os.mkdir(dataFolder)


class GetStats(QObject):

    downloadFinished = pyqtSignal()

    def __init__(self):
        super(GetStats,self).__init__()
        self.keywordQueue = Queue()
        self.keywords=[]
        self.progress=True
        self.currentDownloaded=None


    def setKeywords(self,wordObject):
        self.keywords=wordObject
        file_names = os.listdir(dataFolder)
        for obj in self.keywords:
            t=0
            for j in file_names:
                fileName=j.split("_")[0]
                if obj not in fileName:
                     t+=1
            if t>=len(file_names) or len(file_names)==0:
                self.keywordQueue.put(obj)

        self.getData()

    def getData(self):
        for i in range(5):
            t = Thread(target=getInfoWorker, args=(self.keywordQueue,self.downloadFinished))
            t.start()

        self.keywordQueue.join()

def getInfoWorker(queue,signal):
    """
    Running and emptiing queue

    :param queue: the queue
    :param signal: the signal
    :return:
    """

    while not queue.empty():

        wordObj=queue.get()
        wordData=getWordData(wordObj)
        queue.task_done()

        signal.emit()


def getWordData(keyWord):
    """
    download the google stat of a word from Adwords

    :param keyWord: key word
    :return: dictionary of a word stat from google adwords

    """
    dataDict={}
    dataDictMonth={}

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
    try:
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
            dataDictMonth['Monthly Research']=attributes['TARGETED_MONTHLY_SEARCHES']

            # print('Keyword: "%s" \n average monthly search volume '
            #       '"%s" \n '
            #       'Competition: %s \n '
            #       'Average CPC: %s \n '
            #       'Monthly Average Search: %s'
            #       % (attributes['KEYWORD_TEXT'],
            #         attributes['SEARCH_VOLUME'],
            #         attributes['COMPETITION'],
            #         attributes['AVERAGE_CPC']['microAmount'] / 1000000
            #        ,attributes['TARGETED_MONTHLY_SEARCHES']
            #         ))

        saveData(dataDict,dataDictMonth,keyWord)

        return dataDict
    except:
        return None

def saveData(data,dataDictMonth, keyWord):
    """
    save the dictionary generated by getWordData into a JSON file
    :param data: dataDict of getWordData
    :param keyWord: a keyword from the table wordlist
    :return: saved JSON file for a keyword
    """
    if data:
        with open(dataFolder + keyWord + "_data.json", "w",encoding='utf-8') as dataFile:
            json.dump(data, dataFile,ensure_ascii=False)
        print("saving data for", keyWord)

    if dataDictMonth:
        dict={}
        df = pd.DataFrame()
        for i in dataDictMonth['Monthly Research']:
            dict['year']=i['year']
            dict['month']=i['month']
            dict['count']=i['count']
            jsonDf=pd.DataFrame(dict,index=[0])
            df=df.append(jsonDf, ignore_index=True)

        df.to_csv(dataFolder + keyWord + "_dataMonthly.csv",index=False)
        print("saving dataMonthly for", keyWord)


def delData(folder_path):
    """
    :param folder_path: path of the json files of the DATA directory.
    """

    files=[ f for f in os.listdir(folder_path) ]


    for file in files:
        #print(file)
        os.remove(folder_path + file)

