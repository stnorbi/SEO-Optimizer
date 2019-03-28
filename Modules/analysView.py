#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt4.QtCore import Qt, pyqtSignal

#from PyQt4.QtCore import Signal
import os

#own packages
from Modules import widgets

class AnalysView(QWidget):
    wordsChange=pyqtSignal(list)

    def __init__(self,mainwindow):
        QWidget.__init__(self)
        self.mainWindow=mainwindow
        self.resize(500,500)
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0,10,10,10)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        AnalysLayout=QVBoxLayout()
        self.layout().addLayout(AnalysLayout)

        self.analyserTable=TableWidget(self)
        AnalysLayout.addWidget(self.analyserTable)

        separator = widgets.Separator("horizontal")


class TableWidget(QTableWidget):
    wordsChange = pyqtSignal(list)
    def __init__(self,parent,text):
        QTableWidget.__init__(self,parent)
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


        self.cellChanged.connect(self.setWordList)

    def setWordList(self):
        wordList = []
        allRows = self.rowCount()
        self.setRowCount(allRows+1)
        if self.item(0, 0).text():
            for row in range(0,allRows-1):
                wordList.append(self.item(row,0).text())
        print(wordList)
        return wordList


    # def setComparesion(self,text):
    #     wordList=self.setWordList()
    #     return wordList
        #self.wordsChange.emit(text)
        # if wordList:
        #     for word in wordList:
        #         if word in text:
        #             print("OK")
        # else:
        #     print("error")




    def addNewRow(self):
            self.insertRow(1)

    def refresh(self):
        self.clear()


