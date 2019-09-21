import os, re, subprocess


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

