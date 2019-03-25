#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit
#from PyQt4.QtCore import Signal
import os

#own packages
from Modules import widgets

class dovView:
    def __init__(self,mainwindow):
        QWidget.__init__(self)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,10,10,10)
        self.setContextMenuPolicy(Qt.CustomcontextMenu)

        self.mainWindow=mainwindow
        self.progress=0
        self.movieItems=[]
        self.sorting="alphabet"

        filterLayout = QHBoxLayout()
        self.layout().addLayout(filterLayout)

        separator = widgets.Separator("vertical")
        filterLayout.addWidget(separator)


