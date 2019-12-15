import os, re
from utils import fileUtils
from PyQt5.QtWidgets import QTableWidgetItem

class Word(QTableWidgetItem):
    def __init__(self,name,index):
        QTableWidgetItem.__init__(self)
        self.name=name
        self.index=index
#        self.downloaded=False
        self.fileName=fileUtils.filesPath + self.name
        self.data=fileUtils.readData(self.name,fileUtils.filesPath)

        self.avg_search=None
        self.cmp=None
        self.avg_cpc=None
        self.mth_volume=None


    def getData(self):
        if self.data:
            if "Search Volume" in self.data:
                self.avg_search = self.data["Search Volume"]

            if "CMP" in self.data:
                if self.data["CMP"][0]<=0.4:
                    self.cmp = "alacsony"
                elif 0.4<self.data["CMP"][0]<=0.70:
                    self.cmp="közepes"
                else:
                    self.cmp = "magas"

            if "CPC" in self.data:
                self.avg_cpc = self.data["CPC"]

            if "Monthly Research" in self.data:
                self.mth_volume = self.data["Monthly Research"]



# if __name__ == "__main__":
#     word=Word('majom')
#     print(word.data['Monthly Research'])