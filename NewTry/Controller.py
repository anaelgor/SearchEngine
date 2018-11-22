import os
import pathlib
import time
from NewTry import ReadFile
#from NewTry import  Parser
from NewTry.ReadFile import dic_to_parse


def SendToParser():
    #TODO: send original dictionary to parser
    Parser.parse(dic_to_parse)
    pass

def Main():
    path = 'C:\Retrieval_folder\corpus'
    start = time.time()
    global corpus_path
    corpus_path = path
    for root, dirs, files in os.walk(corpus_path):
        for file in files:
            ReadFile.takeDocsInfoFromOneFile(str(pathlib.PurePath(root, file)))
            SendToParser()
            dic_to_parse.clear()

    docdoc = dic_to_parse
    #saveDictionaryToDisk()
    end = time.time()
    print(end-start)

text ="during which the Cuba-Spain-Unesco lll 6-7 days 9000-kkk between 12 and 13"
splited = text.split()
print (splited)


Main()