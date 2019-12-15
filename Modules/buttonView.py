#third party packages
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QLineEdit
from PyQt5.QtGui import QColor
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


        show_DashBoard = ShowDashboard()
        buttonLayout.addWidget(show_DashBoard)
        #
        # separator = widgets.Separator("horizontal")
        # self.layout().addWidget(separator)


        self.doclist=QListWidget()
        self.layout().addWidget(self.doclist)



    def keyPressEvent(self, event):
        if event.key() == 16777274:
            self.mainWindow.toggleFullScreen()

    def getMailAddress(self):
        emailAddress=emailField



class ShowDashboard(QPushButton):
    def __init__(self):
        QPushButton.__init__(self)
        self.setText("Enable Dashboard")
        self.setCheckable(True)
        self.setChecked(False)


    def turnOn(self,runProcess):
        self.clicked.connect(runProcess)
        self.setChecked(True)
        return self.isChecked()



    def checkedChecker(self,isChecked):
        if isChecked == True:
            self.setText("Dashboard is enabled")
        else:
            self.setText("Enable Dashboard")
