from PyQt4.QtCore import QObject, pyqtSignal
from queue import Queue
import json, os
from threading import Thread

from googleads import adwords

google_yaml=os.path.dirname(__file__).replace('utils','Authentication')+"/"
print(google_yaml)
# Initialize the AdWords client.
adwords_client = adwords.AdWordsClient.LoadFromStorage(google_yaml+"googleads.yaml")

targeting_idea_service = adwords_client.GetService('TargetingIdeaService', version='v201809')

selector = {
    'ideaType': 'KEYWORD',
    'requestType':'STATS',
    }

selector['requestedAttributeTypes'] = [
    'KEYWORD_TEXT', 'SEARCH_VOLUME', 'COMPETITION','AVERAGE_CPC','TARGETED_MONTHLY_SEARCHES']


offset = 0
PAGE_SIZE = 100
selector['paging'] = {
    'startIndex': str(offset),
    'numberResults': str(PAGE_SIZE)
}

selector['searchParameters']=[{
    'xsi_type': 'RelatedToQuerySearchParameter','queries': ['vegán','online marketing','keresőoptimalizálás','hadoop', 'kutya']}
    ,{'xsi_type': 'LocationSearchParameter','locations': {'id': 20415}}
    ,{'xsi_type':'LanguageSearchParameter','languages': {'id':1024}}
    ]
# időkeret felállításának nézz utánaSS

page = targeting_idea_service.get(selector)



for result in page['entries']:
  attributes = {}
  for attribute in result['data']:
    attributes[attribute['key']] = getattr(
        attribute['value'], 'value', '0')
  print ('Keyword: "%s" \n average monthly search volume '
         '"%s" \n Competition: %s \n Average CPC: %s \n Monthly Average Search: %s' % (attributes['KEYWORD_TEXT'],
            attributes['SEARCH_VOLUME'],
            attributes['COMPETITION'],
            attributes['AVERAGE_CPC']['microAmount']/1000000,
            attributes['TARGETED_MONTHLY_SEARCHES']))