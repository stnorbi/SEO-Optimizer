import os, re, subprocess

iconpath=os.path.dirname(__file__).replace("utils",'images')+"/"

def getIcon():
    icons={"mainIcon": iconpath+"mainicon.jpg",
           "mainBackground": iconpath + "mainbackground.jpg"
    }
    return icons

print(getIcon()["mainIcon"])