#Module: backend.py
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_credentials_manager = SpotifyClientCredentials('fcade02a1b2b4585a7fc019836240782', '2ccf5da7375445519b60e1052d8fbfde')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth('fcade02a1b2b4585a7fc019836240782', '2ccf5da7375445519b60e1052d8fbfde',
                                               'http://localhost:8888/callback', scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


def validateEntry(username):
    print(len(str(username)))
    return len(str(username)) > 5

def getTextToSave():
    return "Hello this is a test :)"
