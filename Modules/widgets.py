#third party packages
from PyQt4.QtGui import QFrame, QPushButton, QIcon, QLabel, QPainter, QColor, QBrush, QPen, QCursor, QApplication, \
    QTextEdit, QTableWidget, QTableWidgetItem
from PyQt4.QtCore import QSize, Qt, pyqtSignal,QPointF
from PyQt4.QtGui import (QGraphicsView, QGraphicsScene,
                             QGraphicsEllipseItem, QGraphicsSceneHoverEvent,
                             QGraphicsSceneMouseEvent)

import sys,math
from nltk.tokenize import word_tokenize, wordpunct_tokenize
from nltk.corpus import stopwords
from threading import Thread
from nltk.stem.snowball import SnowballStemmer
import nltk

#own packages
from utils import API, fileUtils
from Modules import word
from Modules import figures

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
        text = self.toPlainText()
        stop_words = set(stopwords.words("hungarian"))
        tokens=wordpunct_tokenize(text)
        text = nltk.Text(tokens)
        #tokens = word_tokenize(text)
        words = [w.lower() for w in text if w.isalpha()]
        raw_words = [w.lower() for w in words if not w in stop_words]
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
        self.cellChanged.connect(self.getKeyWordList)
        self.cellPressed.connect(self.fillTable)
        self.cellDoubleClicked.connect(self.getTooltip)

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
        keyword=self.item(keyword_idx[0],keyword_idx[1]).text()

        if keyword and keyword_idx:
            data = fileUtils.readCSV(keyword, fileUtils.filesPath)
            tooltip=figures.ToolTip()
            tooltip.sortData(data)
            self.getWorker(Thread,tooltip.customPlot,tooltip.data,keyword)


    def getWorker(self,thread,customPlot,data,keyword):
        thread = Thread(target=customPlot, args=[data, keyword])
        thread.setDaemon(True)
        thread.start()




    def rowInserting(self):
        """
        :return: add a new empty row to table widget, if n-th row is not empty
        """
        nr_rows=self.rowCount()
        if self.item(nr_rows-1,0):
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





# if __name__ == '__main__':
#     app = QApplication([])
#     f = MyTooltip()
#     f.show()
#     sys.exit(app.exec_())