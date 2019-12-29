import os
from subprocess import call
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

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
#
# with open(path+"test.txt","w") as file:
#     file.write(text)
#
# os.system("sh "+path + "test.sh")

wordcloud = WordCloud(width=2000, height=800).generate_from_text(text)

# Display the generated image:
plt.figure(figsize=(15,5))
plt.imshow(wordcloud, interpolation='nearest',aspect="equal")
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()