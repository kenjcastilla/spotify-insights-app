from django.http import HttpResponse
from django.shortcuts import redirect
from dotenv import load_dotenv
from os import getenv
from spotipy import SpotifyOAuth, DjangoSessionCacheHandler, Spotify

load_dotenv()
CLIENT_ID = getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = getenv('SPOTIPY_REDIRECT_URI')


def spotify_login(request):
    sp_oauth = SpotifyOAuth(
        scope="user-top-read",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        cache_handler=DjangoSessionCacheHandler(request),
    )

    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


def spotify_callback(request):
    sp_oauth = SpotifyOAuth(
        scope="user-top-read",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        cache_handler=DjangoSessionCacheHandler(request),
    )

    handler = DjangoSessionCacheHandler(request)
    token_info = sp_oauth.get_access_token(check_cache=False)
    handler.save_token_to_cache(token_info)

    spotify = Spotify(oauth_manager=sp_oauth)

    return HttpResponse("Logged in successfully"), spotify
