# spotify-insights-app
A Django app that shows a user's personal Spotify listening insights organized by time frame.

I used the **[Spotipy](https://spotipy.readthedocs.io/en/2.22.1/)** Python library to send requests to Spotify's API instead of constructing and sending the requests myself (see the use of the Python Requests HTTP library in the [Spotify API project](https://github.com/kenjcastilla/spotify-api-project/blob/main/playlist_functions.py) or the Node.js **[Axios](https://axios-http.com/docs/intro)** HTTP library in the [Foodmixr](https://github.com/kenjcastilla/foodmixr-web/blob/main/src/spotify/SetCurrentTrack.js) project).

To use the application, add a .env file to the root directory with the following variables:
    
    SPOTIFY_CLIENT_ID
    
    SPOTIFY_CLIENT_SECRET
    
    SPOTIPY_REDIRECT_URI

Then, simply run the server from the root directory:

    python manage.py runserver

[Demo](https://youtu.be/UuxTPbC4yvY)
