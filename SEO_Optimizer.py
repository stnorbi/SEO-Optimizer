#third party external packages
from PyQt4.QtGui import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPainter, QPixmap, QIcon, \
        QSplitter, QToolBar, QMenuBar
from PyQt4.QtCore import Qt, pyqtSignal, QSettings
import sys, os


#own packages
from utils import fileUtils
from Modules import buttonView, docView, analysView, toolBar
from Modules import widgets

iconPath = os.path.dirname(__file__) + "/images/"

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

        centralWidget=QWidget()
        centralWidget.setLayout(QHBoxLayout())
        centralWidget.layout().setContentsMargins(0,0,0,0)
        self.setCentralWidget(centralWidget)



        viewLayout=QHBoxLayout()
        centralWidget.layout().addLayout(viewLayout)
        splitter = QSplitter(Qt.Vertical)

        editorLayout=QVBoxLayout()
        centralWidget.layout().addLayout(editorLayout)

        # self.separator = widgets.Separator('horizontal')
        # viewLayout.addWidget(self.separator)

        self.buttonView=buttonView.ButtonView(self)
        viewLayout.addWidget(self.buttonView)


        editorLayout.addWidget(splitter)

        self.separator = widgets.Separator('vertical')

        #add TextEditor & Table widget to the splitter
        self.docView=docView.DocView(self)
        splitter.addWidget(self.docView)

        self.analysView=analysView.AnalysView(self)
        splitter.addWidget(self.analysView)

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


    #backend modules
    def setWordList(self):
        self.analysView.setWords()

app=QApplication(sys.argv)
window=SeoOptimizer()
window.show()
app.exec_()
