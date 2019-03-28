#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt4.QtCore import Qt, SIGNAL

#from PyQt4.QtCore import Signal
import os

#own packages
from Modules import widgets, docView

class AnalysView(QWidget):
    def __init__(self,mainwindow):
        QWidget.__init__(self)
        self.resize(500,500)
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0,10,10,10)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        self.mainWindow=mainwindow


        AnalysLayout=QVBoxLayout()
        self.layout().addLayout(AnalysLayout)

        self.analyserTable=QTableWidget()
        self.analyserTable.keyboardGrabber()
        self.analyserTable.setUpdatesEnabled(True)
        self.analyserTable.setColumnCount(7)
        self.analyserTable.setRowCount(1)
        self.analyserTable.resize(400,250)
        self.analyserTable.setHorizontalHeaderLabels(("Szavak;"
                                                      "Megjelenítés;"
                                                      "Pozíció;"
                                                      "CTR;"
                                                      "Kattintás;"
                                                      "Tartalmazza?;"
                                                      ).split(";"))
        AnalysLayout.addWidget(self.analyserTable)

        separator = widgets.Separator("horizontal")


    def setWords(self):
        allRows = self.analyserTable.rowCount()
        if self.analyserTable.cellWidget(1, 1):
            for row in range(0,allRows):
                word=self.analyserTable.cellWidget(row,1)
                print(word)



    def addNewRow(self,rows):
        if self.analyserTable.cellWidget(rows,1):
            rows+=1
            self.analyserTable.setRowCount(rows)