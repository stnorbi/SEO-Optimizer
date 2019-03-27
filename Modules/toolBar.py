from PyQt4.QtGui import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPainter, QPixmap, QIcon, \
        QSplitter, QToolBar, QMenuBar, QAction
from PyQt4.QtCore import Qt
import sys, os


class MenuBar(QMenuBar):
    def __init__(self,mainwindow):
        QMainWindow.__init__(self)

        file=self.addMenu("File")
        edit=self.addMenu("Edit")
        view=self.addMenu("View")

        file.addMenu("New")










