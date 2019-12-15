from PyQt5.QtGui import  QPainter, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QToolBar, QMenuBar
from PyQt5.QtCore import Qt

import sys, os


class MenuBar(QMenuBar):
    def __init__(self,mainwindow):
        QMainWindow.__init__(self)

        file=self.addMenu("File")
        edit=self.addMenu("Edit")
        view=self.addMenu("View")

        file.addMenu("New")










