#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit, QTextEdit, QToolBar, QMenu, QTextDocument
from PyQt4.QtCore import Qt, pyqtSignal
import os

#own packages
from Modules import widgets, analysView

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

        self.textEditor=TextEditor(self)
        editorLayout.addWidget(self.textEditor)

        self.textEditor.textChanged.connect(self.textEditor.slotSignal)

    # def setText(self):
    #     wordList=self.getText()
    #     print(wordList)
    #     self.textChange.emit(wordList)


class TextEditor(QTextEdit):
    pressButton=pyqtSignal(list)
    def __init__(self,mainLayout):
        QTextEdit.__init__(self,mainLayout)

        self.setUpdatesEnabled(True)
        self.createStandardContextMenu()

        self.textChanged.connect(self.getText)

    def getText(self):
        textBoxValue = self.toPlainText().split(' ')
        return textBoxValue


    def slotSignal(self):
        text=self.getText()
        print(text)
        self.pressButton.emit(text)

    #
    # def keyPressEvent(self,*args,**kwargs):
    #     self.pressButton.emit()



