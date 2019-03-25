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

        buttonLayout=QHBoxLayout()
        self.layout().addLayout(buttonLayout)

        emailField=QLineEdit()
        buttonLayout.addWidget(emailField)

        logIn_bttn=QPushButton("Log into Google")
        #logIn_bttn.clicked.connect("") #TODO: set up the connection with google
        buttonLayout.addWidget(logIn_bttn)


        separator=widgets.Separator("vertical")
        self.layout().addWidget(separator)