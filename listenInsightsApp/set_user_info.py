from dotenv import load_dotenv
from os import getenv
# from firebase_config import database
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy import Spotify
from pprint import pprint

load_dotenv()
CLIENT_ID = getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = getenv('SPOTIPY_REDIRECT_URI')


def get_top_tracks():
    """
    Uses spotipy to retrieve current user's top 20 tracks, organized by time range.
    tracks_info = [[track_name, track_artists, album, release_year, track_id, track_uri],...]
    return: results_by_range = {
             'short_term': {tracks_info},
             'medium_term': {tracks_info},
             'long_term': {tracks_info}
            }
    """
    scope = 'user-top-read'
    spotify = Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=scope
        )
    )

    time_ranges = ['short_term', 'medium_term', 'long_term']
    tracks_by_range = {time_range: [] for time_range in time_ranges}

    for time_range in time_ranges:
        results = spotify.current_user_top_tracks(limit=20, time_range=time_range)
        for track in results['items']:
            track_name = track['name']
            track_artists = []
            for i in range(0, len(track['artists'])):
                track_artists.append([track['artists'][i]['name'], track['artists'][i]['id']])
            album = track['album']['name']
            release_year = track['album']['release_date'][:4]
            track_id = track['id']
            track_uri = track['uri']
            tracks_by_range[time_range].append([track_name, track_artists, album, release_year, track_id, track_uri])

    pprint(tracks_by_range)
    return tracks_by_range


def get_top_artists():
    """
    Uses spotipy to retrieve current user's top 20 artists, organized by time range.

    tracks_info = [[artist_name, artist_genres, artist_popularity, artist_id],...]

    return: results_by_range = {
             'short_term': {artists_info},
             'medium_term': {artists_info},
             'long_term': {artists_info}
            }
    """
    scope = 'user-top-read'
    spotify = Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=scope
        )
    )

    time_ranges = ['short_term', 'medium_term', 'long_term']
    artists_by_range = {time_range: [] for time_range in time_ranges}

    for time_range in time_ranges:
        results = spotify.current_user_top_artists(limit=20, time_range=time_range)
        for artist in results['items']:
            artist_name = artist['name']
            artist_genres = artist['genres']
            artist_popularity = artist['popularity']
            artist_id = artist['id']

            artists_by_range[time_range].append([artist_name, artist_genres, artist_popularity, artist_id])

    pprint(artists_by_range)
    return artists_by_range


tracks = get_top_tracks()
artists = get_top_artists()
