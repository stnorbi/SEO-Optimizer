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
        self.analyserTable.setUpdatesEnabled(True)
        #self.analyserTable.setRowCount(50)
        self.analyserTable.setColumnCount(9)
        #self.analyserTable.resize(400,250)
        self.analyserTable.setHorizontalHeaderLabels(("Words;"
                                                      "Metric1;"
                                                      "Metric2;"
                                                      "Metric3;"
                                                      "Metric4;"
                                                      "Metric5;"
                                                      "Metric6;"
                                                      "Metric7;"
                                                      "Metric8;"
                                                      ).split(";"))
        AnalysLayout.addWidget(self.analyserTable)

        separator = widgets.Separator("horizontal")


    def setWords(self,items):
        self.analyserTable.setRowCount(50)
        j=0
        if items:
            for word in items:
                self.analyserTable.setItem(j,0,QTableWidgetItem(QTableWidgetItem(word)))
                j=j+1
                self.analyserTable.update()
        else:
            print("empty")