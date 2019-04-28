#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit, QTextEdit, QTableWidget, QToolBar, QMenu, QSplitter, QTextList
from PyQt4.QtCore import Qt, pyqtSignal
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



#own packages
from Modules import widgets


class Analyser(QWidget):
    changeSignal=pyqtSignal(list)
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

    def setComparesion(self):
        keyWords=self.table.getKeyWordList()
        words=self.textEditor.writeList()
        checkList=[]
        for i in keyWords:
             if i in words:
                 checkList.append("Ok")
             else:
                checkList.append("No")
        print(checkList)
        return checkList

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
        raw_words = [w for w in tokens if not w in stop_words]
        return raw_words


class TableWidget(QTableWidget):
    def __init__(self,parent):
        QTableWidget.__init__(self)

        self.parent=parent

        self.keyboardGrabber()
        self.setUpdatesEnabled(True)
        self.setColumnCount(7)
        self.setRowCount(2)
        self.resize(400,250)
        self.setHorizontalHeaderLabels(("Szavak;"
                                      "Megjelenítés;"
                                      "Pozíció;"
                                      "CTR;"
                                      "Kattintás;"
                                      "Tartalmazza?;"
                                      ).split(";"))


        self.cellEntered.connect(self.addNewRow)


    def addNewRow(self):
        wordList = []
        allRows = self.rowCount()
        keywords=self.getKeyWordList()
        if len(keywords)>0:
            self.setRowCount(allRows + 1)


    def getKeyWordList(self):
        keyWordList = []
        allRows = self.rowCount()
        if self.item(allRows-1,0):
            for row in range(0,allRows):
                keyWordList.append(self.item(row,0).text())
        return keyWordList



    def refresh(self):
        self.clear()