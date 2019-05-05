from utils import API
#from Modules import seoAnalyser
from PyQt4.QtGui import QTableWidgetItem


class KeyWordList(QTableWidgetItem):
    def __init__(self,parent,keyword):
        QTableWidgetItem.__init__(self)
        self.parent=parent

        self.word=keyword
        for i in self.word:
            self.dataFile =  API.dataFolder + i +".json"

        self.avg_search=None
        self.cmp=None
        self.avg_cpc=None
        self.mth_volume=None
        self.data={}

    # def setKeyWordList(self):
    #     keyWords=parent.getKeyWordList()

    def getData(self):
        data = API.getWordData(self.word)

        if data:
            self.data = data
            if "Search Volume" in self.data:
                self.avg_search = self.data["Search Volume"]

            if "CMP" in self.data:
                self.cmp = self.data["CMP"]

            if "CPC" in self.data:
                self.avg_cpc = self.data["CPC"]

            if "Monthly Research" in self.data:
                self.mth_volume = self.data["Monthly Research"]


    def saveData(self):
        for i in self.word:
            API.saveData(self.data, i)

# if __name__ == "__main__":
#     valami=KeyWordList(KeyWordList,'kutya')
#     valami.getData()
#     valami.saveData()
    #print(list(KeyWord('kutya').data['Search Volume'])[0])