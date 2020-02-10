#GUI Libraries
from PyQt5.QtWidgets import  QMainWindow,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem

#Data Processing Libraries
import pandas as pd
import numpy as np
import sys

#Dataviz Libraries
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
from PIL import Image
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from wordcloud import WordCloud

#Own Libraries
from Modules import widgets


class ToolTip(Figure):
    def __init__(self, *args, **kwargs):
        Figure.__init__(self, *args, **kwargs)

        self.fig = plt

        #self.fig.rcParams['figure.facecolor'] = 'yellow'
        self.fig.rcParams["image.aspect"]='auto'

        self.data=None

    def sortData(self,data):
        data = data.sort_values(['year', 'month'], ascending=[True, True])
        data['year'] = data['year'].apply(str)
        data['month'] = data['month'].apply(str)
        data['year_month'] = data['year'] + "-" + data['month']
        self.data=data
        return self.data


    def customPlot(self,data,keyword):

        self.fig.figure(num="SEO TOOL - DataViz")
        self.fig.title('Keresések alakulása ' + keyword + ' kulcsszóra')

        self.setData(data)

        #self.fig.figimage(fileUtils.getIcon()["mainBackground"])

        self.fig.ticklabel_format(style='plain',axis='y', useOffset=False)

        self.fig.xticks(rotation=15)
        self.fig.xlabel('Év - Hónap')
        self.fig.ylabel('Keresések száma')


        #self.fig.imshow(image)

        #self.setBackground(fileUtils.getIcon()["mainBackground"])
        self.showViz()

    def setData(self,data):
        sns.barplot(x='year_month', y="count", data=data)

    def showViz(self):
        self.fig.show()

    def setBackground(self,filePath):
        #image=self.imageResizer(filePath)
        image=self.fig.imread(filePath)
        self.fig.imshow(image,alpha=0.5)#extent=[0, 4000, 0, 1080])

    # def imageResizer(self,filePath):
    #     img=Image.open(filePath)
    #     img = img.resize((5, 10), Image.ANTIALIAS)
    #     return img



class DashBoard(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("SEO Optimizer - TextMining Dashboard")

        #main widget Layout
        centralWidget=QWidget()
        centralWidget.setLayout(QHBoxLayout())
        centralWidget.layout().setContentsMargins(0,0,0,0)
        self.setCentralWidget(centralWidget)


        #other widget layouts
        viewLayout=QHBoxLayout()
        centralWidget.layout().addLayout(viewLayout)

        verticalLeft=QVBoxLayout()
        centralWidget.layout().addLayout(verticalLeft)

        verticalRight=QVBoxLayout()
        centralWidget.layout().addLayout(verticalRight)



        self.canvasRightTop=Canvas(self)
        verticalRight.addWidget(self.canvasRightTop)


        self.canvasRightBottom=Canvas(self)
        verticalRight.addWidget(self.canvasRightBottom)

        self.canvasLeftTop=Canvas(self)
        verticalLeft.addWidget(self.canvasLeftTop)

        self.canvasLeftBottom=QTableWidget(self)
        verticalLeft.addWidget(self.canvasLeftBottom)

        self.table=widgets.TableWidget(self)
        print(self.table.keyWordList.items())


    def tablePlot(self,df,table):
        headers = ["Szavak","Darab"]

        table.setRowCount(df.shape[0])
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        df_index = df.index
        df_value=df.values

        for row in range(len(df_index)):
            table.setItem(row, 0, QTableWidgetItem(str(df_index[row])))
            table.setItem(row, 1, QTableWidgetItem(str(df_value[row][0])))




class Canvas(FigureCanvas):
    def __init__(self,parent=None,width = 15, height = 5, dpi = 100):

        fig=Figure(figsize=(width,height),dpi=dpi)
        # self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self,fig)
        self.setParent(parent)


    def piePlot(self,df,title=None):
        x=[i[0] for i in np.array(df)]
        labels = list(df[df.columns[0]].index)
        self.figure.suptitle(title)
        ax = self.figure.add_subplot(111)
        ax.pie(x, labels=labels,autopct='%1.1f%%')


    def setWordCloud(self,df,WC):
        text=str(df) #df['Default']
        wordcloud = WC(font_path=None, width = 1800, height=1000,
           stopwords=None, max_font_size=None, font_step=1, mode='RGB',
            collocations=True, colormap=None, normalize_plurals=True).generate(text)

        ax=self.figure.add_subplot(111)

        # Display the generated image:
        ax.imshow(wordcloud, interpolation="nearest", aspect="equal")
        ax.axis("off")
        self.figure.tight_layout(pad=0)


    def barPlot(self, text):
        self.table=widgets.TableWidget(self)
        keyWordList=self.table.keyWordList

        print(keyWordList.items())
