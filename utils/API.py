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
    'requestType':'IDEAS'
    }

selector['requestedAttributeTypes'] = [
    'KEYWORD_TEXT', 'SEARCH_VOLUME', 'CATEGORY_PRODUCTS_AND_SERVICES']

offset = 0
PAGE_SIZE = 200
selector['paging'] = {
    'startIndex': str(offset),
    'numberResults': str(PAGE_SIZE)
}

selector['searchParameters'] = [{
    'xsi_type': 'RelatedToQuerySearchParameter',
    'queries': ['space cruise']
}]

page = targeting_idea_service.get(selector)



for result in page['entries']:
  attributes = {}
  for attribute in result['data']:
    attributes[attribute['key']] = getattr(
        attribute['value'], 'value', '0')
  print ('Keyword with "%s" text and average monthly search volume '
         '"%s" was found with Products and Services categories: %s.'
         % (attributes['KEYWORD_TEXT'],
            attributes['SEARCH_VOLUME'],
            attributes['CATEGORY_PRODUCTS_AND_SERVICES']))