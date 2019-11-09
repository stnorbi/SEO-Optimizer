#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit, QTextEdit, QTableWidget, QToolBar, QMenu, QSplitter, QTextList, QTableWidgetItem
from PyQt4.QtCore import Qt, pyqtSignal
import os

from Modules import widgets
from nltk.stem.snowball import SnowballStemmer


#own packages
from Modules import widgets
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

        self.textEditor.textChanged.connect(self.setComparesion)
        #self.table.itemChanged.connect(self.setComparesion)
        self.textEditor.textChanged.connect(self.getComparesion)


    def setComparesion(self):
        '''
        compare the content of the textEditor widget (words) and the words in the analyser table

        :return: boolean "list", JSON (YES/NO) of the words based on findings

        '''
        keyWords=self.table.keyWordList
        words=[self.wordStemmer(i) for i in (self.textEditor.writeList())]
        print(words)

        for k,v in keyWords.items():
            t=self.wordStemmer(v)
            print(t)
            if t in words:
                 self.checkList[k]="Ok"
            else:
                self.checkList[k]="No"
        self.comparesion.emit(self.checkList)
        return self.checkList

    def wordStemmer(self,raw_word):
        stemmer = SnowballStemmer('hungarian')
        stemmed=stemmer.stem(raw_word)

        return stemmed

    def getComparesion(self):
        '''
        write the result of words comparesion into 5th or 4th column of the analyser table

        '''
        for k,v in self.checkList.items():
            #if self.table.isColumnHidden(4)==True:
            self.table.setItem(k,5,QTableWidgetItem(v))





