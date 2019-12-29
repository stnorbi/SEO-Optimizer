import httplib2

from apiclient import errors
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
import os,json

credPath=os.path.dirname(__file__)+"/client_secrets.json"
print(credPath)


with open(credPath) as file:
    credFile=json.load(file)

CLIENT_ID="980410190140-8krd8dorbqqdg7paj3r7a8tnag4rlr6d.apps.googleusercontent.com"
CLIENT_SECRET ="bPXUtfsESnGFHMvT4MSzmBtB"

OAUTH_SCOPE = 'https://www.googleapis.com/auth/webmasters.readonly'
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
