#third party external packages
from PyQt4.QtGui import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPainter, QPixmap, QIcon
from PyQt4.QtCore import Qt
import sys, os


#own packages
from utils import fileUtils
from Modules import buttonView, docView
from Modules import widgets

iconPath = os.path.dirname(__file__) + "/images/"

class SeoOptimizer(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("SEO Optimizer - Content Tool")
        self.setWindowIcon(QIcon(fileUtils.getIcon()["mainIcon"]))
        self.resize(1350,900)


        centralWidget=QWidget()
        centralWidget.setLayout(QVBoxLayout())
        centralWidget.layout().setContentsMargins(0,0,0,0)
        self.setCentralWidget(centralWidget)


        viewLayout=QVBoxLayout()
        centralWidget.layout().addLayout(viewLayout)


        self.separator = widgets.Separator('vertical')
        viewLayout.addWidget(self.separator)

        self.buttonView=buttonView.ButtonView(self)
        viewLayout.addWidget(self.buttonView)

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
