#third party packages
from PyQt4.QtGui import QFrame, QPushButton, QIcon, QLabel, QPainter, QColor, QBrush, QPen, QCursor, QApplication, \
    QTextEdit, QTableWidget
from PyQt4.QtCore import QSize, Qt, pyqtSignal,QPointF
from PyQt4.QtGui import (QGraphicsView, QGraphicsScene,
                             QGraphicsEllipseItem, QGraphicsSceneHoverEvent,
                             QGraphicsSceneMouseEvent)

import sys

#own packages


class Separator(QFrame):
    def __init__(self, type="horizontal"):
        super(Separator, self).__init__()
        self.setObjectName("separator")
        if type == "horizontal":
            self.setFrameShape(QFrame.HLine)
        else:
            self.setFrameShape(QFrame.VLine)



# class ToolTip(QGraphicsEllipseItem):
#     def __init__(self, top_left_x, top_left_y, radius):
#         super().__init__(0, 0, radius, radius)
#         self.setPos(top_left_x, top_left_y)
#         self.setBrush(Qt.red)
#         self.setAcceptHoverEvents(True)
#
#         self.setToolTip("Test")
#
#     def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
#         QApplication.instance().setOverrideCursor(Qt.OpenHandCursor)
#
#     def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
#         QApplication.instance().restoreOverrideCursor()
#
#     def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent'):
#         new_cursor_position   = event.scenePos()
#         old_cursor_position   = event.lastScenePos()
#         old_top_left_corner   = self.scenePos()
#         new_top_left_corner_x = new_cursor_position.x() - old_cursor_position.x() + old_top_left_corner.x()
#         new_top_left_corner_y = new_cursor_position.y() - old_cursor_position.y() + old_top_left_corner.y()
#         self.setPos(QPointF(new_top_left_corner_x, new_top_left_corner_y))
#
#     def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'): pass
#
#     def mouseDoubleClickEvent(self, event: 'QGraphicsSceneMouseEvent'): pass
#
#     def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent'):
#         self.setToolTip("<h3>pos: <hr>x({}), y({})</h3>"                  # < +++++
#                         "".format(self.pos().x(), self.pos().y()))
#
# class MyTooltip(QGraphicsView):
#     def __init__(self):
#         super().__init__()
#         self.scene = QGraphicsScene()
#         self.setScene(self.scene)
#         self.setSceneRect(0, 0, 250, 250)
#         self.disk = ToolTip(50, 50, 20)
#         self.scene.addItem(self.disk)

# if __name__ == '__main__':
#     app = QApplication([])
#     f = MyTooltip()
#     f.show()
#     sys.exit(app.exec_())