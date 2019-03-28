import os, re, subprocess


iconpath=os.path.dirname(__file__).replace("utils",'images')+"/"

def getIcon():
    icons={"mainIcon": iconpath+"mainIcon.jpg",
           "mainBackground": iconpath + "mainbackground.jpg"
    }
    return icons

def getText(text):
    print(text)


