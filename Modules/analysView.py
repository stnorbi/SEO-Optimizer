#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt4.QtCore import Qt, SIGNAL

#from PyQt4.QtCore import Signal
import os

#own packages
from Modules import widgets, docView

class AnalysView(QWidget):
    wordsChange=SIGNAL('list')

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

        self.analyserTable.cellChanged.connect(self.analyserTable.setWordList)


class TableWidget(QTableWidget):
    def __init__(self,parent):
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


    def setWordList(self):
        wordList=[]
        allRows = self.rowCount()
        self.setRowCount(allRows+1)
        if self.item(0, 0).text():
            for row in range(0,allRows-1):
                wordList.append(self.item(row,0).text())
        return wordList



    def addNewRow(self):
            self.insertRow(1)

    def refresh(self):
        self.clear()