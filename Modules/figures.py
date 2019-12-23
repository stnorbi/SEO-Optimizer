#third party packages
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
from PIL import Image
import pyqtgraph as pg
import sys
from PyQt5.QtWidgets import  QMainWindow,QApplication, QWidget, QVBoxLayout, QHBoxLayout





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
    def __init__(self, *args, **kwargs):
        super(DashBoard,self).__init__(*args, **kwargs)

        self.setWindowTitle("SEO Optimizer - TextMining Dashboard")

        #main widget Layout
        centralWidget=QWidget()
        centralWidget.setLayout(QHBoxLayout())
        centralWidget.layout().setContentsMargins(0,0,0,0)
        self.setCentralWidget(centralWidget)


        #other widget layouts
        viewLayout=QHBoxLayout()
        centralWidget.layout().addLayout(viewLayout)

        self.graphWidget = pg.PlotWidget(self)
        viewLayout.addWidget(self.graphWidget)


        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]




        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)


    def main():
        app = QApplication(sys.argv)
        main = DashBoard()
        main.show()
        sys.exit(app.exec_())


if __name__=='__main__':
    DashBoard.main()