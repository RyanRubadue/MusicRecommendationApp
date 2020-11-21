#Module: backend.py
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import os
import spotipy.util as util


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

#Retrieves the user's most listened to artists over the specified time period
def getTopArtists():
    scope = "user-top-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth('fcade02a1b2b4585a7fc019836240782', '2ccf5da7375445519b60e1052d8fbfde',
                                                  'http://localhost:8888/callback', scope=scope))
    token = util.prompt_for_user_token('ryanrubby', scope, 'fcade02a1b2b4585a7fc019836240782', '2ccf5da7375445519b60e1052d8fbfde',
                        'http://localhost:8888/callback')

    texts = []
    results = sp.current_user_top_artists(time_range='medium_term', limit=20)

    for i, item in enumerate(results['items']):
        texts.append(str(i+1) + ". " + item['name'])
    return texts

#Retrieves the user's most listened to tracks over the specified time period
def getTopTracks():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth('fcade02a1b2b4585a7fc019836240782', '2ccf5da7375445519b60e1052d8fbfde',
                                                  'http://localhost:8888/callback', scope=scope))
    token = util.prompt_for_user_token('ryanrubby', scope, 'fcade02a1b2b4585a7fc019836240782', '2ccf5da7375445519b60e1052d8fbfde',
                                                   'http://localhost:8888/callback')
    texts = []
    results = sp.current_user_top_tracks(time_range='medium_term', limit=20)

    for i, item in enumerate(results['items']):
        texts.append(str(i+1) + '. ' + item['name'] + ' ' + item['artists'][0]['name'])
    return texts

    ##TODO Add choice of time period to display top songs for (short, medium long)
