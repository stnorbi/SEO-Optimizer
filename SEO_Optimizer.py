from PyQt4.QtGui import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPainter, QPixmap, QIcon
from PyQt4.QtCore import Qt
import sys, os


class SeoOptimizer(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("SEO Optimizer - Content Tool")



app=QApplication(sys.argv)
window=SeoOptimizer()
window.show()
app.exec_()
