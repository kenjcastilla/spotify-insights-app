from django.shortcuts import render
from django.views import generic
# from firebase_config import database
from .set_user_info import get_top_tracks, get_top_artists, get_tracks_stats, get_artists_stats

top_tracks = get_top_tracks()
top_artists = get_top_artists()
# Create your views here.


def index_view(request):
    template = "spotifyInsightsApp/index.html"

    return render(request, template)


class HistoryView(generic.DetailView):
    # song_titles = database.child('Data')
    longtime = 6


def top_short_term_view(request):
    template = "spotifyInsightsApp/short-term.html"

    top_tracks_short_term = top_tracks['short_term']
    top_artists_short_term = top_artists['short_term']

    context = get_context(top_tracks_short_term, top_artists_short_term)

    return render(request, template, context)


def top_medium_term_view(request):
    template = "spotifyInsightsApp/medium-term.html"

    top_tracks_medium_term = top_tracks['medium_term']
    top_artists_medium_term = top_artists['medium_term']

    context = get_context(top_tracks_medium_term, top_artists_medium_term)

    return render(request, template, context)


def top_long_term_view(request):
    template = "spotifyInsightsApp/long-term.html"

    top_tracks_long_term = top_tracks['long_term']
    top_artists_long_term = top_artists['long_term']

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
