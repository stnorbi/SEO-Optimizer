#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit, QTableWidget
from PyQt4.QtCore import Qt

#from PyQt4.QtCore import Signal
import os

#own packages
from Modules import widgets

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
        self.analyserTable.setRowCount(50)
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