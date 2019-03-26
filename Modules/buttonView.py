#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit
#from PyQt4.QtCore import Signal
import os

#own packages
from Modules import widgets

class ButtonView(QWidget):
    def __init__(self,mainWindow):
        QWidget.__init__(self)
        self.setMaximumWidth(350)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(10,10,0,10)
        self.mainWindow=mainWindow

        buttonLayout = QVBoxLayout()
        self.layout().addLayout(buttonLayout)

        emailField = QLineEdit()
        emailField.setPlaceholderText("Mail Address")

        logIn_bttn = QPushButton("Log into Google")
        # logIn_bttn.clicked.connect("") #TODO: set up the connection with google

        sync_bttn=QPushButton('Sync with Google Drive')


        buttonLayout.addWidget(emailField)
        buttonLayout.addWidget(logIn_bttn)
        buttonLayout.addWidget(sync_bttn)

        separator = widgets.Separator("horizontal")
        self.layout().addWidget(separator)


        self.doclist=QListWidget()
        self.layout().addWidget(self.doclist)



    def keyPressEvent(self, event):
        if event.key() == 16777274:
            self.mainWindow.toggleFullScreen()

    def getMailAddress(self):
        emailAddress=emailField