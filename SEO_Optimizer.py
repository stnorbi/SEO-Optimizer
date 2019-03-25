#third party external packages
from PyQt4.QtGui import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPainter, QPixmap, QIcon
from PyQt4.QtCore import Qt
import sys, os


#own packages
from utils import fileUtils
from Modules import buttonView

iconPath = os.path.dirname(__file__) + "/images/"

class SeoOptimizer(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowOpacity(0.8)
        self.setWindowTitle("SEO Optimizer - Content Tool")
        self.setWindowIcon(QIcon(fileUtils.getIcon()["mainIcon"]))
        self.resize(800,600)


        centralWidget=QWidget()
        centralWidget.windowOpacity()
        centralWidget.setLayout(QVBoxLayout())
        centralWidget.layout().setContentsMargins(0,0,0,0)

        viewLayout=QHBoxLayout()
        centralWidget.layout().addLayout(viewLayout)

        self.buttonView=buttonView.ButtonView(self)
        viewLayout.addWidget(self.buttonView)


    def paintEvent(self,event):
        painter=QPainter(self)
        bgPixmap=QPixmap(fileUtils.getIcon()["mainBackground"])
        painter.setOpacity(0.5)
        painter.drawPixmap(self.rect(),bgPixmap)

    def setStyle(self):
        with open(iconPath)


app=QApplication(sys.argv)
window=SeoOptimizer()
window.show()
app.exec_()
