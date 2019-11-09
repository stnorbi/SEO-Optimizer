
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
from PIL import Image




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



class DashBoard(Figure):
    pass
#        self.wordCounter(self.textEditor.writeList())