#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit, QTextEdit, QTableWidget, QToolBar, QMenu, QSplitter, QTextList, QTableWidgetItem
from PyQt4.QtCore import Qt, pyqtSignal
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



#own packages
from Modules import widgets


class Analyser(QWidget):
    comparesion=pyqtSignal(dict)
    def __init__(self,mainwindow):
        QWidget.__init__(self)
        self.mainwindow=mainwindow
        self.resize(500,500)
        self.setLayout(QVBoxLayout())
        #self.layout().setContentsMargins(0,10,10,10)
        #self.setContextMenuPolicy(Qt.CustomContextMenu)

        analyserLayout=QVBoxLayout()
        self.layout().addLayout(analyserLayout)

        splitter = QSplitter(Qt.Vertical)
        analyserLayout.addWidget(splitter)

        #instance of text editor
        self.textEditor=TextEditor(self)
        splitter.addWidget(self.textEditor)

        #instance of tabble
        self.table=TableWidget(self)
        splitter.addWidget(self.table)


        self.textEditor.textChanged.connect(self.setComparesion)
        self.table.itemChanged.connect(self.setComparesion)
        self.textEditor.textChanged.connect(self.getComparesion)



    def setComparesion(self):
        keyWords=self.table.getKeyWordList()
        words=self.textEditor.writeList()
        # print(keyWords.keys())
        # print(words)
        self.checkList={}
        for k,v in keyWords.items():
             if v in words:
                 self.checkList[k]="Ok"
             else:
                self.checkList[k]="No"
        for i in self.checkList.items(): print(i)
        self.comparesion.emit(self.checkList)
        return self.checkList

    def getComparesion(self):
        for k,v in self.checkList.items():
            self.table.setItem(k,5,QTableWidgetItem(v))


class TextEditor(QTextEdit):
    textSignal=pyqtSignal(list)
    def __init__(self,parent):
        QTextEdit.__init__(self)

        self.parent=parent

        self.setUpdatesEnabled(True)
        self.createStandardContextMenu()



    def writeList(self):
        text = self.toPlainText()
        stop_words = set(stopwords.words("hungarian"))
        tokens = word_tokenize(text)
        raw_words = [w.lower() for w in tokens if not w in stop_words]
        return raw_words


class TableWidget(QTableWidget):
    cellValue=pyqtSignal(dict)
    def __init__(self,parent):
        QTableWidget.__init__(self)

        self.parent=parent

        self.keyboardGrabber()
        self.setUpdatesEnabled(True)
        self.setColumnCount(7)
        self.setRowCount(5000)
        self.resize(400,250)
        self.setHorizontalHeaderLabels(("Szavak;"
                                      "Megjelenítés;"
                                      "Pozíció;"
                                      "CTR;"
                                      "Kattintás;"
                                      "Tartalmazza?;"
                                      ).split(";"))
    # def addNewRow(self,wlist):
    #     wordList=wlist
    #     allRows = self.rowCount()
    #     if len(wordList)>=1:
    #        self.insertRow(allRows)

    def getKeyWordList(self):
        keyWordList = {}
        allRows = self.rowCount()
        for row in range(0,allRows):
            if self.item(row, 0):
                keyWordList[row]= self.item(row,0).text().lower()
        self.cellValue.emit(keyWordList)
        return keyWordList



    def refresh(self):
        self.clear()
