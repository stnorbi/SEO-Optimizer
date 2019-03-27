import pandas as pd
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
import subprocess


#read authentication file
keyFile=os.path.dirname(__file__)+"/Authentication/Youtube Analyser-2920d371ed7e.json"


credentials=ServiceAccountCredentials.from_json_keyfile_name(keyFile,['https://www.googleapis.com/auth/documents.readonly'])
drive_cred=ServiceAccountCredentials.from_json_keyfile_name(keyFile,['https://www.googleapis.com/auth/drive.metadata.readonly'])
#client=gspread.authorize(credentials)

DOCUMENT_ID='1faAl80i1P3OsDbNMUurlg_Qyavy7Jb3NA4H3ZYf5PCM'

#doc=client.open_by_url(url_for_doc)
service = build('docs', 'v1', credentials=credentials)
drive = build('drive', 'v3', credentials=drive_cred)

#TODO: innen folytasd!!!
results=drive.changes().execute()
print(results)

for i in results['changes']:
    print(i)




document = service.documents().get(documentId=DOCUMENT_ID).execute()
# print(document.items(),"\n")
# print(document.keys(),"\n")


# while True:
#     document = service.documents().get(documentId=DOCUMENT_ID).execute()
#     for i in range(1,len(document['body']['content'])):
#         print(document['body']['content'][i]['paragraph']['elements'][0]['textRun']['content'])
#     os.system("clear")




#print(document['body']['content'][2]['paragraph']['elements'][0]['textRun']['content'])
#[1]['paragraph']['elements'][0]['textRun']['content']
