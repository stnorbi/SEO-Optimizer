#third party external packages
from PyQt5.QtGui import  QPainter, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QToolBar, QMenuBar
from PyQt5.QtCore import Qt, pyqtSignal, QSettings
import sys, os


#own packages
from utils import fileUtils
from Modules import buttonView, toolBar
from Modules import widgets, seoAnalyser
from utils import API

iconPath = os.path.dirname(__file__) + "/images/"
dataPath=os.path.dirname(__file__) + "/Data/"

class SeoOptimizer(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("SEO Optimizer - Content Tool")
        self.setWindowIcon(QIcon(fileUtils.getIcon()["mainIcon"]))
        self.resize(1350,900)

        self.settings=QSettings("StNorbi Soft", "SEO-Optimizer")
        if self.settings.value("geometry"):
            self.restoreGeometry(self.settings.value("geometry"))

        menubar=toolBar.MenuBar(self)
        self.setMenuBar(menubar)

        #splitter
        splitter = QSplitter(Qt.Horizontal)


        #mainwindow layout
        centralWidget=QWidget()
        centralWidget.setLayout(QHBoxLayout())
        centralWidget.layout().setContentsMargins(0,0,0,0)
        self.setCentralWidget(centralWidget)


        #other widget layouts
        viewLayout=QHBoxLayout()
        centralWidget.layout().addLayout(viewLayout)


        self.buttonView=buttonView.ButtonView(self)
        splitter.addWidget(self.buttonView)


        analysLayout=QVBoxLayout()
        centralWidget.layout().addLayout(analysLayout)


        #add TextEditor & Table widget to the splitter
        self.analyser=seoAnalyser.Analyser(self)
        splitter.addWidget(self.analyser)


        centralWidget.layout().addWidget(splitter)

        self.setStyle()

    def paintEvent(self,event):
        painter=QPainter(self)
        bgPixmap=QPixmap(fileUtils.getIcon()["mainBackground"])
        #painter.setOpacity(0.5)
        painter.drawPixmap(self.rect(),bgPixmap)

    def setStyle(self):
        with open(iconPath + 'style.qss', "r") as qss_file:
            self.setStyleSheet(qss_file.read())


    def closeEvent(self,*args,**kwargs):
        self.settings.setValue("geometry",self.saveGeometry())
        API.delData(dataPath)
        text=self.analyser.textEditor.toPlainText()
        #fileUtils.saveText(text)



    #backend modules
    def setWordList(self):
        self.analysView.setWords()




app=QApplication(sys.argv)
window=SeoOptimizer()
window.show()
app.exec_() 
