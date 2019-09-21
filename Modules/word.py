import os, re
from utils import API

class Word():
    def __init__(self,name,path):
        self.name=name
        self.downloaded=False
        self.dataFile=API.filesPath + self.title