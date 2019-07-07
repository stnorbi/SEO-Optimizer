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
        self.table.itemChanged.connect(self.setComparesion)
        self.textEditor.textChanged.connect(self.getComparesion)


    # def set_WordList(self):
    #     keyWords=self.table.getKeyWordList()
    #     words=[]
    #     for k,v in keyWords.items():
    #         words.append(v)
    #     return words


    def setComparesion(self):
        '''
        compare the content of the textEditor widget (words) and the words in the analyser table

        :return: boolean "list", JSON (YES/NO) of the words based on findings

        '''
        keyWords=self.table.keyWordList
        words=self.textEditor.writeList()
        self.checkList={}
        for k,v in keyWords.items():
            #self.table.setItem(k, 1, QTableWidgetItem(list(keywordStats.KeyWord('kutya').data['Search Volume'])[0]))
            if v in words:
                 self.checkList[k]="Ok"
            else:
                self.checkList[k]="No"
        self.comparesion.emit(self.checkList)
        return self.checkList

    def getComparesion(self):
        '''
        write the result of words comparesion into 5th column of the analyser table

        '''
        for k,v in self.checkList.items():
            self.table.setItem(k,5,QTableWidgetItem(v))


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
        self.setRowCount(1)
        self.resize(400,250)
        self.setHorizontalHeaderLabels(("Szavak;"
                                      "Átlag keresés;"
                                      "Verseny;"
                                      "Átlag CPC;"
                                      "Kattintás;"
                                      "Tartalmazza?;"
                                      ).split(";"))
        self.keyWordList={}
        self.cellPressed.connect(self.getTooltip)
        self.cellChanged.connect(self.getKeyWordList)


    # def addNewRow(self,wlist):
    #     wordList=wlist
    #     allRows = self.rowCount()
    #     if len(wordList)>=1:
    #        self.insertRow(allRows)

    def getKeyWordList(self):
        keyWords=[]
        allRows = self.rowCount()
        #self.dataDownload(word)
        self.rowdelet()
        for row in range(0,allRows):
            if self.item(row, 0):
                word=self.item(row,0).text().lower()
                self.dataDownload(word)
                self.keyWordList[row]= self.item(row,0).text().lower()
                #keyWords.append(word)

        self.rowInserting()

        self.cellValue.emit(self.keyWordList)
        return self.keyWordList

    def getTooltip(self):
        keyword_idx=[self.currentRow(),0]
        keyword=self.item(keyword_idx[0],keyword_idx[1])
        if keyword:
            self.setToolTip(keyword.text())

    def dataDownload(self,words):
        """
        Download and save the Adwords related numbers into JSON file (per word).
        Only the new words have been downloaded.

        :param words: list of words from the table
        :return: the JSON files of keywords
        """
        file_names=os.listdir(filesPath)
        t=0
        for j in file_names:
            if words not in j:
                t+=1
        if t==len(file_names) or len(file_names)==0:
            wordList = keywordStats.KeyWordList(self,words)
            wordList.getData()
            wordList.saveData()


    def rowInserting(self):
        """
        :return: add a new empty row to table widget
        """
        nr_rows=self.rowCount()
        if self.item(nr_rows-1,0):
            if len(self.item(nr_rows-1,0).text())!=0:
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

