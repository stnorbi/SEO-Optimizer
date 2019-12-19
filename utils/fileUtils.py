import os, re, subprocess
import json
import pandas as pd


iconpath=os.path.dirname(__file__).replace("utils",'images')+"/"
#textPath=os.path.dirname(__file__).replace("utils",'Data')+"/"

filesPath=os.path.dirname(__file__).replace('utils','Data')+ '/'

#FilePath for TextMining module
textPath=os.path.dirname(__file__).replace('utils','TextMining') + '/hunlp-pipeline/'

def getIcon():
    icons={"mainIcon": iconpath+"mainIcon.jpg",
           "mainBackground": iconpath + "mainbackground.jpg"
    }
    return icons

def getText(textPath):
    with open(textPath + "test.txt", "r") as file:
        text=file.read()


def saveText(text):
    print(text)
    with open(textPath + "test.txt","w") as file:
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

def readPOS(textPath):
    headers = ["Raw Words", "Default", "POS", "Word & POS"]
    df=pd.read_csv(textPath+"test.txt.ana",sep='\t',header=None)
    df.columns = headers
    return df