#third party packages
from PyQt4.QtGui import QFrame, QPushButton, QIcon, QLabel, QPainter, QColor, QBrush, QPen, QCursor, QApplication
from PyQt4.QtCore import QSize, Qt

#own packages


class Separator(QFrame):
    def __init__(self, type="horizontal"):
        super(Separator, self).__init__()
        self.setObjectName("separator")
        if type == "horizontal":
            self.setFrameShape(QFrame.HLine)
        else:
            self.setFrameShape(QFrame.VLine)