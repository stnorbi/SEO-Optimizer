DIRPATH=/media/norbert/Datas/Python/SEO_Content_Tool/TextMining/hunlp-pipeline/
echo ${DIRPATH}
#export BASEPATH=${DIRPATH}hunlp-pipeline


sh ${DIRPATH}010.huntoken < ${DIRPATH}test.txt > ${DIRPATH}test.txt.tok
sh ${DIRPATH}011.hunpos-hunmorph < ${DIRPATH}test.txt.tok > ${DIRPATH}test.txt.posmorph
python ${DIRPATH}012.stem -m --morphdel '||' ${DIRPATH}test.txt.posmorph ${DIRPATH}test.txt.stem
python ${DIRPATH}013.chooseana.py ${DIRPATH}test.txt.stem > ${DIRPATH}test.txt.ana
