from spotipy import CacheHandler


class CustomCacheHandler(CacheHandler):
    def __init__(self, request):
        self.request = request

    def get_cached_token(self):
        return self.request.session.get("spotify_token")

    def save_token_to_cache(self, token_info):
        print(f'SAVE_TOKEN_TO_CACHE--Token Info: {token_info}')
        self.request.session["spotify_token"] = token_info

    def delete_token_info(self):
        self.request.session.pop("spotify_token", None)
