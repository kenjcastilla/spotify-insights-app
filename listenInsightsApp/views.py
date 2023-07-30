from django.shortcuts import render
from django.views import generic
# from firebase_config import database
from set_user_info import get_top_tracks, get_top_artists

top_tracks = get_top_tracks()
top_artists = get_top_artists()
# Create your views here.


class IndexView(generic.ListView):
    template_name = "listenInsightsApp/index.html"


class HistoryView(generic.DetailView):
    # song_titles = database.child('Data')
    longtime = 6


class TopShortTermView(generic.DetailView):
    template_name = "listenInsightsApp/topshortterm.html"
    top_tracks_short_term = top_tracks['short_term']
    track_names = [track[0] for track in top_tracks_short_term]
    track_artists = [track[1] for track in top_tracks_short_term]
    track_albums = [track[2] for track in top_tracks_short_term]
    track_release_years = [track[3] for track in top_tracks_short_term]

    top_artists_short_term = top_artists['short_term']
    artist_names = [artist[0] for artist in top_artists_short_term]
    artist_genres = [artist[1] for artist in top_artists_short_term]
    artist_popularity = [artist[2] for artist in top_artists_short_term]


class TopMediumTermView(generic.DetailView):
    template_name = "listenInsightsApp/topmediumterm.html"
    top_tracks_medium_term = top_tracks['medium_term']
    track_names = [track[0] for track in top_tracks_medium_term]
    track_artists = [track[1] for track in top_tracks_medium_term]
    track_albums = [track[2] for track in top_tracks_medium_term]
    track_release_years = [track[3] for track in top_tracks_medium_term]

    top_artists_medium_term = top_artists['medium_term']
    artist_names = [artist[0] for artist in top_artists_medium_term]
    artist_genres = [artist[1] for artist in top_artists_medium_term]
    artist_popularity = [artist[2] for artist in top_artists_medium_term]


class TopLongTermView(generic.DetailView):
    template_name = "listenInsightsApp/toplongterm.html"
    top_tracks_long_term = top_tracks['long_term']
    track_names = [track[0] for track in top_tracks_long_term]
    track_artists = [track[1] for track in top_tracks_long_term]
    track_albums = [track[2] for track in top_tracks_long_term]
    track_release_years = [track[3] for track in top_tracks_long_term]

    top_artists_long_term = top_artists['long_term']
    artist_names = [artist[0] for artist in top_artists_long_term]
    artist_genres = [artist[1] for artist in top_artists_long_term]
    artist_popularity = [artist[2] for artist in top_artists_long_term]
