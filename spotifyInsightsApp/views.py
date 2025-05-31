import time
from os import getenv
from .custom_cache_handler import CustomCacheHandler
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect
from dotenv import load_dotenv
from spotipy import SpotifyOAuth, Spotify
from .set_user_info import get_top_tracks, get_top_artists, get_tracks_stats, get_artists_stats
from .spotify_auth import get_spotify_client

load_dotenv()
CLIENT_ID = getenv('SPOT_CLIENT_ID')
CLIENT_SECRET = getenv('SPOT_CLIENT_SECRET')
REDIRECT_URI = getenv('SPOTIPY_REDIRECT_URI')


class UserData:
    def __init__(self):
        self.top_tracks: dict = {}
        self.top_artists: dict = {}


user_data = UserData()


def spotify_callback(request):
    sp_oauth = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-top-read",
        cache_handler=CustomCacheHandler(request),
    )
    print('SPOTIFY_CALLBACK--session info:', request.session.__dict__, '\n')
    code_from_session = request.GET.get('code')
    print('SPOTIFY_CALLBACK--code from session:', code_from_session)
    # print(f"SPOTIFY_CALLBACK--code in cache: {cache.get('code')}")
    # print(f'SPOTIFY_CALLBACK--Code: {code}\n')
    if code_from_session:
        token_info = sp_oauth.get_access_token(code=code_from_session)
        spotify = Spotify(auth=token_info, auth_manager=sp_oauth)
        user_data.top_tracks = get_top_tracks(spotify, request)
        user_data.top_artists = get_top_artists(spotify)

        return redirect('spotifyInsightsApp:index')

    return HttpResponse("Authentication failed")

# Create your views here.


def perform_checks(request, redirect_url):
    cache_handler = CustomCacheHandler(request)
    token = cache_handler.get_cached_token()
    print(f'PERFORM-CHECKS--Token from cache: {token}')
    print('PERFORM-CHECKS--Current time:', time.time(), '\n')

    if not token \
            or time.time() >= token['expires_at'] \
            or not user_data.top_tracks \
            or not user_data.top_artists:
        get_spotify_client(request)
        spotify_callback(request)


def index_view(request):
    template = "spotifyInsightsApp/index.html"
    cache_handler = CustomCacheHandler(request)
    token = cache_handler.get_cached_token()
    print(f'INDEX--Token from cache: {token}')
    print('INDEX--Current time:', time.time(), '\n')

    if not token \
            or time.time() >= token['expires_at'] \
            or not user_data.top_tracks \
            or not user_data.top_artists:
        client_info = get_spotify_client(request)
        print(f'INDEX--returned from get_spotify_client(): {client_info}')
        if type(client_info) is not str:
            print(f'INDEX--http response info: {client_info.url}')
            redirect(client_info.url)
        else:
            token = client_info
    spotify = Spotify(auth=token)
    # response = spotify_callback(request)
    # if not spotify:
    #     return redirect("spotifyInsightsApp:auth-error")
    user_data.top_tracks = get_top_tracks(spotify, request)
    user_data.top_artists = get_top_artists(spotify)

    return render(request, template)


def auth_error_view(request):
    template = "spotifyInsightsApp/auth-error.html"

    return render(request, template)


def top_short_term_view(request):
    # perform_checks(request, "spotifyInsightsApp:short-term")
    if not user_data.top_tracks or not user_data.top_artists:
        return redirect("spotifyInsightsApp:index")

    template = "spotifyInsightsApp/short-term.html"

    top_tracks_short_term = user_data.top_tracks['short_term']
    top_artists_short_term = user_data.top_artists['short_term']

    context = get_context(top_tracks_short_term, top_artists_short_term)

    return render(request, template, context)


def top_medium_term_view(request):
    perform_checks(request, "spotifyInsightsApp:medium-term")
    # if not user_data.top_tracks or not user_data.top_artists:
    #     return redirect("spotifyInsightsApp:index")

    template = "spotifyInsightsApp/medium-term.html"

    top_tracks_medium_term = user_data.top_tracks['medium_term']
    top_artists_medium_term = user_data.top_artists['medium_term']

    context = get_context(top_tracks_medium_term, top_artists_medium_term)

    return render(request, template, context)


def top_long_term_view(request):
    perform_checks(request, "spotifyInsightsApp:long-term")
    # if not user_data.top_tracks or not user_data.top_artists:
    #     return redirect("spotifyInsightsApp:index")

    template = "spotifyInsightsApp/long-term.html"

    top_tracks_long_term = user_data.top_tracks['long_term']
    top_artists_long_term = user_data.top_artists['long_term']

    context = get_context(top_tracks_long_term, top_artists_long_term)
    return render(request, template, context)


def get_context(tracks, artists):
    """
    Construct and return context given track and artist information for
        a given amount of time.
    Input: top_tracks and top_artists (of a specific term)
    Return: context for term view
    """
    track_names = [track[0] for track in tracks]
    track_urls = [track[-1] for track in tracks]
    track_artist_names = [track[1][0] for track in tracks]
    track_artist_urls = [track[1][1] for track in tracks]
    track_album_titles = [track[2] for track in tracks]
    track_album_urls = [track[3] for track in tracks]
    album_release_years = [track[4] for track in tracks]

    artist_names = [artist[0] for artist in artists]
    artist_urls = [artist[-1] for artist in artists]
    artist_genres = [artist[1] for artist in artists]
    artist_popularity_scores = [artist[2] for artist in artists]

    mode_album_release_year, oldest_track_idx, newest_track_idx = get_tracks_stats(album_release_years)
    mean_pop_score, min_pop_score_idx, max_pop_score_idx = get_artists_stats(artist_popularity_scores)

    context = {
        "track_names": track_names,
        "track_urls": track_urls,
        "track_artist_names": track_artist_names,
        "track_artist_urls": track_artist_urls,
        "track_album_titles": track_album_titles,
        "track_album_urls": track_album_urls,
        "album_release_years": album_release_years,
        "artist_names": artist_names,
        "artist_urls": artist_urls,
        "artist_genres": artist_genres,
        "artist_popularity_scores": artist_popularity_scores,
        "mode_album_release_year": mode_album_release_year,
        "oldest_track_idx": oldest_track_idx,
        "newest_track_idx": newest_track_idx,
        "mean_pop_score": mean_pop_score,
        "min_pop_score_idx": min_pop_score_idx,
        "max_pop_score_idx": max_pop_score_idx,
    }

    return context
