#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit, QTextEdit
from PyQt4.QtCore import Qt, SIGNAL
import os

#own packages
from Modules import widgets

class DocView(QWidget):
    def __init__(self,mainwindow):
        QWidget.__init__(self)
        self.resize(500,500)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,10,10,10)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        self.mainWindow=mainwindow


        editorLayout=QVBoxLayout()
        self.layout().addLayout(editorLayout)

        self.textEditor=QTextEdit()
        self.textEditor.setUpdatesEnabled(True)
        self.textEditor.createStandardContextMenu()
        editorLayout.addWidget(self.textEditor)

        separator = widgets.Separator("vertical")
#        filterLayout.addWidget(separator)

    def getText(self):
        textBoxValue=self.textEditor.toPlainText()

