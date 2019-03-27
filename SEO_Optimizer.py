#third party external packages
from PyQt4.QtGui import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPainter, QPixmap, QIcon
from PyQt4.QtCore import Qt
import sys, os


#own packages
from utils import fileUtils
from Modules import buttonView, docView, analysView
from Modules import widgets

iconPath = os.path.dirname(__file__) + "/images/"

class SeoOptimizer(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("SEO Optimizer - Content Tool")
        self.setWindowIcon(QIcon(fileUtils.getIcon()["mainIcon"]))
        self.resize(1350,900)


        centralWidget=QWidget()
        centralWidget.setLayout(QHBoxLayout())
        centralWidget.layout().setContentsMargins(0,0,0,0)
        self.setCentralWidget(centralWidget)


        viewLayout=QHBoxLayout()
        centralWidget.layout().addLayout(viewLayout)

        editorLayout=QVBoxLayout()
        centralWidget.layout().addLayout(editorLayout)

        # self.separator = widgets.Separator('horizontal')
        # viewLayout.addWidget(self.separator)

        self.buttonView=buttonView.ButtonView(self)
        viewLayout.addWidget(self.buttonView)

        self.separator = widgets.Separator('vertical')
        viewLayout.addWidget(self.separator)

        self.docView=docView.DocView(self)
        editorLayout.addWidget(self.docView)

        self.analysView=analysView.AnalysView(self)
        editorLayout.addWidget(self.analysView)
        self.setStyle()



    def paintEvent(self,event):
        painter=QPainter(self)
        bgPixmap=QPixmap(fileUtils.getIcon()["mainBackground"])
        #painter.setOpacity(0.5)
        painter.drawPixmap(self.rect(),bgPixmap)

    def setStyle(self):
        with open(iconPath + 'style.qss', "r") as qss_file:
            self.setStyleSheet(qss_file.read())





app=QApplication(sys.argv)
window=SeoOptimizer()
window.show()
app.exec_()
