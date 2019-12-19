import os
from subprocess import call
import subprocess
import pandas as pd
import matplotlib.pyplot as plt


text="""
Harcos típus, nagy küzdő. Ha lesz esélye, a gyógyulásban is ki fogja használni.
Ennek így nem lehet vége. Imádkozom érte, és meggyőződésem, viszontlátjuk őt. Szeretném megfogni a kezét, a szemébe nézni,
átölelni. Corinna azonban elutasította a jelenlétem. Valószínűleg attól tart, ha találkozom velük, elmondom másoknak is,
amit látok.
"""

# text="""
#     Mindenki megcsinálja a maga hülyeségét, ha kell ha nem. Ahogy elindultak az erdőbe visszataláltak a helyes
#     ösvényre.
#     """

"/media/norbert/Datas/Python/SEO_Content Tool/TextMining/"
path=os.path.dirname(__file__).replace('testing','TextMining') + '/hunlp-pipeline/'
osPath='/media/norbert/Datas/Python/SEO_Content_Tool/TextMining/hunlp-pipeline/'

with open(path+"test.txt","w") as file:
    file.write(text)

os.system("sh "+path + "test.sh")

# Importing POS data
headers=["Raw Words","Default","POS","Word & POS"]
df=pd.read_csv(path+"test.txt.ana",sep='\t',header=None)
df.columns=headers



# Cut & Split POS(es)
df=df[["Raw Words","Default","POS"]]
df["POS"]=df["POS"].str.split("<",expand=True)


df.column="POS_HU"
posTrans={
    "NOUN" : "Főnév"
    ,"ART" : "Névelő"
    , "VERB" : "Ige"
    , "ADJ" : "Melléknév"
    , "ADV" : "Határozószó"
    , "PUNCT" : "Központozás"
    , "CONJ" : "Kötőszó"
    , "PREV" : "Melléknévi igenév"
}

# Translating POS(es)
for k,v in posTrans.items():
    df.loc[df['POS'] == k, 'POS_HU'] = v




print(df)

wordsPOS=df[["POS_HU","Default"]] #for calculation

aggregation=wordsPOS.groupby("POS_HU").count() #count distribution by POS

wordCount=df.groupby("Default").count() # for repeating checker

print(aggregation)
print(wordCount)


# aggregation.plot.pie(y="Default",legend=False,autopct='%1.1f%%', fontsize=8)
# plt.show()


