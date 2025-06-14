from dotenv import load_dotenv
from os import getenv
from spotipy import Spotify
from pprint import pprint
from statistics import mean, mode
from .custom_cache_handler import CustomCacheHandler

load_dotenv()
CLIENT_ID = getenv('SPOT_CLIENT_ID')
CLIENT_SECRET = getenv('SPOT_CLIENT_SECRET')
REDIRECT_URI = getenv('SPOTIPY_REDIRECT_URI')

def get_top_tracks(request):
    """
    Uses spotipy to retrieve current user's top 20 tracks, organized by time range.
    tracks_info = [[track_name, track_artists, album, release_year, track_id, track_uri],...]
    return: results_by_range = {
             'short_term': {tracks_info},
             'medium_term': {tracks_info},
             'long_term': {tracks_info}
            }
    """
    cache_handler = CustomCacheHandler(request)
    token = cache_handler.get_cached_token()
    print(f'GET_TOP_TRACKS--token from custom_cache_handler: {token['access_token']}')
    spotify = Spotify(auth=token['access_token'])
    print(f'GET_TOP_TRACKS--Spotify object: {spotify}')
    print(f'GET_TOP_TRACKS--session info: {request.session.__dict__}\n')
    time_ranges = ['short_term', 'medium_term', 'long_term']
    tracks_by_range = {time_range: [] for time_range in time_ranges}

    for time_range in time_ranges:
        results = spotify.current_user_top_tracks(limit=20, time_range=time_range)
        for track in results['items']:
            track_name = track['name']
            track_artists = [[], []]
            for i in range(0, len(track['artists'])):
                track_artists[0].append(track['artists'][i]['name'])
                track_artists[1].append(track['artists'][i]['external_urls']['spotify'])
            album_title = track['album']['name']
            album_url = track['album']['external_urls']['spotify']
            release_year = track['album']['release_date'][:4]
            track_id = track['id']
            track_uri = track['uri']
            track_url = track['external_urls']['spotify']
            tracks_by_range[time_range].append([track_name, track_artists, album_title, album_url, release_year, track_id, track_uri, track_url])

    pprint(tracks_by_range)
    return tracks_by_range


def get_top_artists(request):
    """
    Uses spotipy to retrieve current user's top 20 artists, organized by time range.

    tracks_info = [[artist_name, artist_genres, artist_popularity, artist_id],...]

    return: results_by_range = {
             'short_term': {artists_info},
             'medium_term': {artists_info},
             'long_term': {artists_info}
            }
    """

    cache_handler = CustomCacheHandler(request)
    token = cache_handler.get_cached_token()
    spotify = Spotify(auth=token['access_token'])

    time_ranges = ['short_term', 'medium_term', 'long_term']
    artists_by_range = {time_range: [] for time_range in time_ranges}

    for time_range in time_ranges:
        results = spotify.current_user_top_artists(limit=20, time_range=time_range)
        for artist in results['items']:
            artist_name = artist['name']
            artist_genres = artist['genres']
            artist_popularity = artist['popularity']
            artist_id = artist['id']
            artist_url = artist['external_urls']['spotify']

            artists_by_range[time_range].append([artist_name, artist_genres, artist_popularity, artist_id, artist_url])

    pprint(artists_by_range)
    return artists_by_range


def get_tracks_stats(release_years):
    """
    Provides information about top tracks.
    return: mode_release_year_idx, oldest_track_idx, newest_track_idx
    """
    mode_release_year_idx, oldest_track_idx, newest_track_idx = mode(release_years), 0, 0
    for idx, year in enumerate(release_years):
        if year < release_years[oldest_track_idx]:
            oldest_track_idx = idx
        if year > release_years[newest_track_idx]:
            newest_track_idx = idx

    return mode_release_year_idx, oldest_track_idx, newest_track_idx


def get_artists_stats(popularity_scores):
    """
    Provides information about top artists.
    return: mean_pop_score_idx, min_pop_score_idx, max_pop_score_idx
    """
    mean_pop_score_idx, min_pop_score_idx, max_pop_score_idx = mean(popularity_scores), -1, -1
    for idx, score in enumerate(popularity_scores):
        if score < popularity_scores[min_pop_score_idx]:
            min_pop_score_idx = idx
        if score > popularity_scores[max_pop_score_idx]:
            max_pop_score_idx = idx

    return mean_pop_score_idx, min_pop_score_idx, max_pop_score_idx
