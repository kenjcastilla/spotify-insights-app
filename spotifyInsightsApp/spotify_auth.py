from django.http import HttpResponse
from django.shortcuts import redirect
from dotenv import load_dotenv
from os import getenv
from spotipy import SpotifyOAuth, Spotify
from .custom_cache_handler import CustomCacheHandler

load_dotenv()
CLIENT_ID = getenv('SPOT_CLIENT_ID')
CLIENT_SECRET = getenv('SPOT_CLIENT_SECRET')
REDIRECT_URI = getenv('SPOTIPY_REDIRECT_URI')


def get_spotify_client(request):
    sp_oauth = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-top-read",
        cache_handler=CustomCacheHandler(request),
    )
    print(f'GET_SPOTIFY_CLIENT--session info: {request.session.__dict__}\n')
    token_info = sp_oauth.get_cached_token()

    print(f'GET_SPOTIFY_CLIENT--token_info: {token_info}\n')
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        print(f'GET_SPOTIFY_CLIENT--redirecting to auth_url: {auth_url}')
        return redirect(auth_url)

    access_token = token_info['access_token']
    print(f'GET_SPOTIFY_CLIENT--access token: {access_token}')

    return access_token
