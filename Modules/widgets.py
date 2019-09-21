#third party packages
from PyQt4.QtGui import QFrame, QPushButton, QIcon, QLabel, QPainter, QColor, QBrush, QPen, QCursor, QApplication, \
    QTextEdit, QTableWidget, QTableWidgetItem
from PyQt4.QtCore import QSize, Qt, pyqtSignal,QPointF
from PyQt4.QtGui import (QGraphicsView, QGraphicsScene,
                             QGraphicsEllipseItem, QGraphicsSceneHoverEvent,
                             QGraphicsSceneMouseEvent)

import sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

#own packages
from utils import API
from Modules import word


class Separator(QFrame):
    def __init__(self, type="horizontal"):
        super(Separator, self).__init__()
        self.setObjectName("separator")
        if type == "horizontal":
            self.setFrameShape(QFrame.HLine)
        else:
            self.setFrameShape(QFrame.VLine)



class TextEditor(QTextEdit):
    textSignal=pyqtSignal(list)
    def __init__(self,parent):
        QTextEdit.__init__(self)

        self.parent=parent

        self.setUpdatesEnabled(True)
        self.createStandardContextMenu()

    #TODO: Ha van mentett szöveg a Data könyvtárban, akkor itt inicializáld, hogy
    #       belekerüljön a szövegszerkesztőbe.


    def writeList(self):
        stemmer=SnowballStemmer('hungarian')
        text = self.toPlainText()
        stop_words = set(stopwords.words("hungarian"))
        tokens = word_tokenize(text)
        raw_words = [w.lower() for w in tokens if not w in stop_words]
        #stemmed=[stemmer.stem(x) for x in tokens]
        return raw_words


class TableWidget(QTableWidget):
    cellValue=pyqtSignal(dict)
    def __init__(self,parent):
        QTableWidget.__init__(self)

        self.parent=parent

        self.keyboardGrabber()
        self.setUpdatesEnabled(True)
        self.setColumnCount(7)
        self.setRowCount(1)
        self.resize(400,250)
        self.setHorizontalHeaderLabels(("Szavak;"
                                      "Átlag keresés;"
                                      "Verseny;"
                                      "Átlag CPC;"
                                      "Kattintás;"
                                      "Tartalmazza?;"
                                      ).split(";"))
        self.setColumnHidden(4,True)

        self.GetStats=API.GetStats()
        self.keyWordList={}
        self.cellPressed.connect(self.getTooltip)
        self.cellChanged.connect(self.getKeyWordList)
        self.cellDoubleClicked.connect(self.fillTable)

        #TODO: Tedd Disable-re a szavakon kívüli oszlopok módosítását.


    def fillTable(self):
        """

        :return: write the Google Adwords metric to the QTableWidget
        """

        w=[]
        wordProperty=self.keyWordList
        #item = QTableWidgetItem("Szuper")
        #self.setItem(0,1,item)
        for k,v in wordProperty.items():
            w=word.Word(v,k)
            w.getData()
            if w.name == v:
                item=QTableWidgetItem(str(w.avg_search[0]))
                self.setItem(k,1,item)


                item=QTableWidgetItem(str(w.cmp))
                self.setItem(k,2,item)


                item=QTableWidgetItem(str(w.avg_cpc[0]))
                self.setItem(k,3,item)


    def getKeyWordList(self):
        """


        :return: keyWordList dictionary. Its keys are the row indexes.
        """

        keyWords=[]
        wordobjects=[]
        allRows = self.rowCount()
        #self.dataDownload(word)
        self.rowdelet()
        for row in range(0,allRows):
            if self.item(row, 0):
                word=self.item(row,0).text().lower()
                self.keyWordList[row]= self.item(row,0).text().lower()
                wordobjects.append(word)

        self.rowInserting()

        self.GetStats.setKeywords(wordobjects)

        self.cellValue.emit(self.keyWordList)

        return self.keyWordList

    def getTooltip(self):
        keyword_idx=[self.currentRow(),0]
        keyword=self.item(keyword_idx[0],keyword_idx[1])
        if keyword:
            w = word.Word(keyword, keyword_idx)
            #self.setToolTip(w.mth_volume)
            self.setToolTip(keyword.text())

    def dataDownload(self,words):
        """
        Download and save the Adwords related numbers into JSON file (per word).
        Only the new words have been downloaded.

        :param words: list of words from the table
        :return: the JSON files of keywords
        """
        # file_names=os.listdir(filesPath)
        # t=0
        # for j in file_names:
        #     if words not in j:
        #         t+=1
        # if t==len(file_names) or len(file_names)==0:
        #     wordList = keywordStats.KeyWordList(self,words)
        #     wordList.getData()
        #     wordList.saveData()


    def rowInserting(self):
        """
        :return: add a new empty row to table widget
        """
        nr_rows=self.rowCount()
        if self.item(nr_rows-1,0):
            #if len(self.item(nr_rows-1,0).text())!=0:
                # item = QTableWidgetItem()
                # #item.setFlags(item.flags() | Qt.ItemIsSelectable)
                # self.setItem(nr_rows, 5, item)
           self.insertRow(nr_rows)




    def rowdelet(self):
        """
        :return: delet the last empty row if the former cell is empty in column 1
        """
        nr_rows = self.rowCount()

        if self.item(nr_rows-1,0) is None or len(self.item(nr_rows-1,0).text())==0:
            self.removeRow(nr_rows-1)
        if len(self.currentItem().text())==0:
            self.removeRow(self.currentRow())

    def refresh(self):
        self.clear()








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