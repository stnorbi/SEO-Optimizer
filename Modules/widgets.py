#third party packages
from PyQt4.QtGui import QFrame, QPushButton, QIcon, QLabel, QPainter, QColor, QBrush, QPen, QCursor, QApplication, \
    QTextEdit, QTableWidget
from PyQt4.QtCore import QSize, Qt, pyqtSignal

#own packages


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


    def getText(self):
        textBoxValue = self.toPlainText().split(' ')

    # def setText(self):
    #     wordList=self.getText()
    #     print(wordList)
    #     self.textChange.emit(wordList)

    #
    # def keyPressEvent(self,*args,**kwargs):
    #     self.pressButton.emit()


class TableWidget(QTableWidget):
    def __init__(self,parent):
        QTableWidget.__init__(self)

        self.parent=parent

        self.keyboardGrabber()
        self.setUpdatesEnabled(True)
        self.setColumnCount(7)
        self.setRowCount(2)
        self.resize(400,250)
        self.setHorizontalHeaderLabels(("Szavak;"
                                      "Megjelenítés;"
                                      "Pozíció;"
                                      "CTR;"
                                      "Kattintás;"
                                      "Tartalmazza?;"
                                      ).split(";"))


    def setWordList(self):
        wordList = []
        allRows = self.rowCount()
        self.setRowCount(allRows+1)
        if self.item(0, 0).text():
            for row in range(0,allRows-1):
                wordList.append(self.item(row,0).text())
        print(wordList)
        return wordList


    # def setComparesion(self,text):
    #     wordList=self.setWordList()
    #     return wordList
        #self.wordsChange.emit(text)
        # if wordList:
        #     for word in wordList:
        #         if word in text:
        #             print("OK")
        # else:
        #     print("error")




    def addNewRow(self):
            self.insertRow(1)

    def refresh(self):
        self.clear()