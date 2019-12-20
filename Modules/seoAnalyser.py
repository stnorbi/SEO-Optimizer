#Front-End (third party) packages
from PyQt5.QtGui import  QColor, QTextList
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QToolBar, QMenu, QListWidget, QPushButton, QFileDialog,\
                            QListWidgetItem, QLineEdit, QTextEdit, QTableWidget, QSplitter, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal, QSettings

#Back-End packages
import os
from collections import Counter
from nltk.stem.snowball import SnowballStemmer
from nltk import chunk
import nltk

#Packages for TextMining
import subprocess
import pandas as pd
import matplotlib.pyplot as plt


#own packages
from Modules import widgets, buttonView
from utils import API, fileUtils

#filesPath=os.path.dirname(__file__).replace('Modules','Data')+ '/'

class Analyser(QWidget):
    comparesion=pyqtSignal(dict)
    def __init__(self,mainwindow):
        QWidget.__init__(self)
        self.mainwindow=mainwindow
        self.resize(500,500)
        self.setLayout(QVBoxLayout())
        #self.layout().setContentsMargins(0,10,10,10)
        #self.setContextMenuPolicy(Qt.CustomContextMenu)

        self.checkList={}

        analyserLayout=QVBoxLayout()
        self.layout().addLayout(analyserLayout)

        splitter = QSplitter(Qt.Vertical)
        analyserLayout.addWidget(splitter)

        #instance of text editor
        self.textEditor=widgets.TextEditor(self)
        splitter.addWidget(self.textEditor)

        #instance of table
        self.table=widgets.TableWidget(self)
        splitter.addWidget(self.table)

        #Connecting to Signal
        self.textEditor.textChanged.connect(self.setComparesion)
        #self.table.itemChanged.connect(self.setComparesion)
        self.textEditor.textChanged.connect(self.getComparesion)


        #instance of stemmer
        self.stemmer = SnowballStemmer('hungarian')

    def setComparesion(self):
        '''
        compare the content of the textEditor widget (words) and the words in the analyser table

        :return: boolean "list", JSON (YES/NO) of the words based on findings

        '''
        keyWords=self.table.keyWordList
        words=[self.wordStemmer(i) for i in (self.textEditor.writeList())]

        for k,v in keyWords.items():
            t=self.wordStemmer(v)
            if t in words:
                 self.checkList[k]="Ok"
            else:
                self.checkList[k]="No"
        self.comparesion.emit(self.checkList)
        #self.wordEntities(self.textEditor.writeList())
        return self.checkList

    def wordStemmer(self,raw_word):
        stemmed=self.stemmer.stem(raw_word)

        return stemmed

    def getComparesion(self):
        '''
        write the result of words comparesion into 5th or 4th column of the analyser table

        '''
        for k,v in self.checkList.items():
            #if self.table.isColumnHidden(4)==True:
            self.table.setItem(k,5,QTableWidgetItem(v))


class TextMiner:
    #textmining=pyqtSignal(str)
    def __init__(self):

        self.posTrans = {
            "NOUN": "Főnév"
            , "ART": "Névelő"
            , "VERB": "Ige"
            , "ADJ": "Melléknév"
            , "ADV": "Határozószó"
            , "PUNCT": "Központozás"
            , "CONJ": "Kötőszó"
            , "PREV": "Melléknévi igenév"
        }

        # self.button=buttonView.ShowDashboard(self)
        # self.button.turnOn(self.preProcess)

    def getText(self):
        text=widgets.TextEditor(self).textWriter()
        #text=fileUtils.getText(fileUtils.textPath)
        return text

    def posTagger(self,text):
        """
        Determine the "Parts of Speech" of the words written in the TextBox

        Return: POS of the words as text file in '/TextMining/hunlp-pipeline/test.txt.ana'
        """
        os.system("sh "+fileUtils.textPath + "test.sh")


    def preProcess(self):
        text=self.getText()
        self.posTagger(text)
        df=fileUtils.readPOS(fileUtils.textPath)
        df = df[["Raw Words", "Default", "POS"]]
        df["POS"] = df["POS"].str.split("<", expand=True)

        for k, v in self.posTrans.items():
            df.loc[df['POS'] == k, 'POS_HU'] = v

        self.df=df
        print(self.df.head())
        return self.df


    def posWordCount(self,df):
        wordsPOS = df[["POS_HU", "Default"]]
        wordsPOS.groupby("POS_HU").count()

        self.posCount=wordsPOS

        return self.posCount


    def worker(self):
        pass

