#third party packages
from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QFileDialog, \
    QListWidgetItem, QColor, QLineEdit, QTextEdit, QTableWidget, QToolBar, QMenu, QSplitter, QTextList, QTableWidgetItem
from PyQt4.QtCore import Qt, pyqtSignal
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Modules import widgets



#own packages
from Modules import widgets, keywordStats

filesPath=os.path.dirname(__file__).replace('Modules','Data')+ '/'



class Analyser(QWidget):
    comparesion=pyqtSignal(dict)
    def __init__(self,mainwindow):
        QWidget.__init__(self)
        self.mainwindow=mainwindow
        self.resize(500,500)
        self.setLayout(QVBoxLayout())
        #self.layout().setContentsMargins(0,10,10,10)
        #self.setContextMenuPolicy(Qt.CustomContextMenu)

        analyserLayout=QVBoxLayout()
        self.layout().addLayout(analyserLayout)

        splitter = QSplitter(Qt.Vertical)
        analyserLayout.addWidget(splitter)

        #instance of text editor
        self.textEditor=TextEditor(self)
        splitter.addWidget(self.textEditor)

        #instance of tabble
        self.table=TableWidget(self)
        splitter.addWidget(self.table)


        self.textEditor.textChanged.connect(self.setComparesion)
        #self.table.itemChanged.connect(self.setComparesion)
        self.textEditor.textChanged.connect(self.getComparesion)



    # def set_WordList(self):
    #     keyWords=self.table.getKeyWordList()
    #     words=[]
    #     for k,v in keyWords.items():
    #         words.append(v)
    #     return words


    def setComparesion(self):
        keyWords=self.table.getKeyWordList()
        words=self.textEditor.writeList()
        kw_list = keyWords.values()
        self.dataDownload(kw_list)
        # print(keyWords.keys())
        # print(words)
        self.checkList={}
        for k,v in keyWords.items():
            #self.table.setItem(k, 1, QTableWidgetItem(list(keywordStats.KeyWord('kutya').data['Search Volume'])[0]))
            if v in words:
                 self.checkList[k]="Ok"
            else:
                self.checkList[k]="No"
        for i in self.checkList.items(): print(i)
        self.comparesion.emit(self.checkList)
        return self.checkList

    def getComparesion(self):
        for k,v in self.checkList.items():
            self.table.setItem(k,5,QTableWidgetItem(v))


    def dataDownload(self,words):
        file_names=os.listdir(filesPath)
        print(file_names)
        for i in words:
            if i not in file_names:
                wordList = keywordStats.KeyWordList(self,words)
                wordList.getData()
                wordList.saveData()


class TextEditor(QTextEdit):
    textSignal=pyqtSignal(list)
    def __init__(self,parent):
        QTextEdit.__init__(self)

        self.parent=parent

        self.setUpdatesEnabled(True)
        self.createStandardContextMenu()



    def writeList(self):
        text = self.toPlainText()
        stop_words = set(stopwords.words("hungarian"))
        tokens = word_tokenize(text)
        raw_words = [w.lower() for w in tokens if not w in stop_words]
        return raw_words


class TableWidget(QTableWidget):
    cellValue=pyqtSignal(dict)
    def __init__(self,parent):
        QTableWidget.__init__(self)

        self.parent=parent

        self.keyboardGrabber()
        self.setUpdatesEnabled(True)
        self.setColumnCount(7)
        self.setRowCount(5000)
        self.resize(400,250)
        self.setHorizontalHeaderLabels(("Szavak;"
                                      "Átlag keresés;"
                                      "Verseny;"
                                      "Átlag CPC;"
                                      "Kattintás;"
                                      "Tartalmazza?;"
                                      ).split(";"))

        self.cellPressed.connect(self.getTooltip)




    # def addNewRow(self,wlist):
    #     wordList=wlist
    #     allRows = self.rowCount()
    #     if len(wordList)>=1:
    #        self.insertRow(allRows)

    def getKeyWordList(self):
        keyWords=[]
        keyWordList = {}
        allRows = self.rowCount()
        for row in range(0,allRows):
            if self.item(row, 0):
                keyWordList[row]= self.item(row,0).text().lower()
                keyWords.append(self.item(row,0).text().lower())
        self.cellValue.emit(keyWordList)
        return keyWordList

    def getTooltip(self):
        keyword_idx=[self.currentRow(),0]
        keyword=self.item(keyword_idx[0],keyword_idx[1])
        if keyword:
            self.setToolTip(keyword.text())



    def refresh(self):
        self.clear()

