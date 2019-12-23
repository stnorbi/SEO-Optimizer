#third party packages
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QLineEdit
from PyQt5.QtGui import QColor
#from PyQt4.QtCore import Signal
import os
import matplotlib.pyplot as plt

#own packages
from Modules import widgets, seoAnalyser

class ButtonView(QWidget):
    def __init__(self,mainWindow):
        QWidget.__init__(self)
        self.setMaximumWidth(350)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(10,10,0,10)
        self.mainWindow=mainWindow

        buttonLayout = QVBoxLayout()
        self.layout().addLayout(buttonLayout)


        show_DashBoard = ShowDashboard(self)
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
    def __init__(self,parent):
        QPushButton.__init__(self)

        self.parent=parent

        self.setText("Enable Dashboard")
        self.setCheckable(True)
        self.setChecked(False)

        self.turnOn(self.runTextMining)


    def turnOn(self,runProcess):
        self.clicked.connect(runProcess)
        # self.setChecked(True)
        # self.checkedChecker(self.isChecked())
        return self.isChecked()

    def checkedChecker(self,isChecked):
        if isChecked == True:
            self.setText("Dashboard is enabled")
        else:
            self.setText("Enable Dashboard")

    def runTextMining(self):
        textMiner = seoAnalyser.TextMiner()
        df=textMiner.preProcess()
        posWordCount=textMiner.posWordCount(df)

        self.setChecked(True)
        self.checkedChecker(self.isChecked())

        #testing
        aggregation = posWordCount.groupby("POS_HU").count()
        aggregation.plot.pie(y="Default",legend=False,autopct='%1.1f%%', fontsize=8)
        plt.show()