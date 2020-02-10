#third party packages
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QLineEdit
from PyQt5.QtGui import QColor
import os
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud as WC

#own packages
from Modules import widgets, seoAnalyser, figures

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

        # separator = widgets.Separator("horizontal")
        # self.layout().addWidget(separator)


        self.doclist=QListWidget()
        self.layout().addWidget(self.doclist)

        # run child methods
        show_DashBoard.turnOn(show_DashBoard.runTextMining)

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
        # df=textMiner.preProcess()

        #Doing further calculation
        posWordCount=textMiner.posCount
        repeatedWords=textMiner.wordCounter(textMiner.data)

        self.dashBoard=figures.DashBoard()
        self.dashBoard.canvasRightTop.piePlot(posWordCount,'Szófajok megoszlása')
        self.dashBoard.tablePlot(repeatedWords,self.dashBoard.canvasLeftBottom)
        self.dashBoard.canvasRightBottom.setWordCloud(textMiner.data['Default'],WC)
        self.dashBoard.canvasLeftTop.barPlot('text')

        self.dashBoard.show()

        self.setChecked(True)
        self.checkedChecker(self.isChecked())


    def plotDataViz(self):
        self.runTextMining()
