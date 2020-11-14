#Module: backend.py
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import GUIFunctionalityv2

client_credentials_manager = SpotifyClientCredentials('fcade02a1b2b4585a7fc019836240782', '2ccf5da7375445519b60e1052d8fbfde')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#scope = "user-library-read"
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth('fcade02a1b2b4585a7fc019836240782', '2ccf5da7375445519b60e1052d8fbfde',
                                               #'http://localhost:8888/callback', scope=scope))

#results = sp.current_user_saved_tracks()

#for idx, item in enumerate(results['items']):
#    track = item['track']
#    print(idx,  , " – ", track['name'])

def validateEntry(username):
    print(len(str(username)))
    return len(str(username)) > 5

def getTextToSave():
    return "Hello this is a test :)"

def getTopArtists():
    scope = "user-top-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth('fcade02a1b2b4585a7fc019836240782', '2ccf5da7375445519b60e1052d8fbfde',
                                                   'http://localhost:8888/callback', scope=scope))
    texts = []
    results = sp.current_user_top_artists(time_range='medium_term', limit=20)

    for i, item in enumerate(results['items']):
        texts.append(str(i+1) + " " + item['name'])
    GUIFunctionalityv2.ResultPage.loadResults(texts, 3)

def getTopTracks():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth('fcade02a1b2b4585a7fc019836240782', '2ccf5da7375445519b60e1052d8fbfde',
                                                   'http://localhost:8888/callback', scope=scope))
    texts = []
    results = sp.current_user_top_tracks(time_range='medium_term', limit=20)
    for i, item in enumerate(results['items']):
        texts.append(str(i+1) + ' ' + item['name'] + ' ' + item['artists'][0]['name'])
    GUIFunctionalityv2.ResultPage.loadResults(texts,2)
    ##TODO Add choice of time period to display top songs for (short, medium long)
