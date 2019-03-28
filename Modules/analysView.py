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

        self.analyserTable=widgets.TableWidget(self)
        AnalysLayout.addWidget(self.analyserTable)

        self.texteditor=widgets.TextEditor(self)

        separator = widgets.Separator("horizontal")

        self.getWords()

    def getWords(self):
        text=self.texteditor.getText()
        wordList=self.analyserTable.setWordList()
        print(text, wordList)
