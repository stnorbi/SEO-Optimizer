import os, re, subprocess
import json
import pandas as pd


iconpath=os.path.dirname(__file__).replace("utils",'images')+"/"
textPath=os.path.dirname(__file__).replace("utils",'Data')+"/"

filesPath=os.path.dirname(__file__).replace('utils','Data')+ '/'

def getIcon():
    icons={"mainIcon": iconpath+"mainIcon.jpg",
           "mainBackground": iconpath + "mainbackground.jpg"
    }
    return icons

def getText(text):
    pass

def saveText(text):

    with open(textPath + "baseText.txt","w") as file:
        file.write(text)

def readData(word,filePath):
    file=filePath + word + "_data.json"
    with open(file) as json_file:
        data=json.load(json_file)
    return data


def readCSV(word,filePath):
    file=filePath + word + "_dataMonthly.csv"
    data=pd.read_csv(file)
    return data

