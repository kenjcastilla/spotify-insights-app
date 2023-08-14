# spotify-insights-app
Provide a Django app that shows a user's personal Spotify listening insights organized by time frame.
I used the Spotipy Python library to perform requests to Spotify's API, as opposed to using my own requests as I did in the [Foodmixr](https://github.com/kenjcastilla/foodmixr-web) project.

To use, add a .env file to the root directory with the following variables:
    
    SPOTIFY_CLIENT_ID
    
    SPOTIFY_CLIENT_SECRET
    
    SPOTIPY_REDIRECT_URI
