from django.shortcuts import render
from django.views import generic
# from firebase_config import database
from .set_user_info import get_top_tracks, get_top_artists, get_tracks_stats, get_artists_stats
from statistics import mean, mode

top_tracks = get_top_tracks()
top_artists = get_top_artists()
# Create your views here.


class IndexView(generic.ListView):
    template_name = "listenInsightsApp/index.html"
    def get_queryset(self):
        """Returns index page."""
        return

class HistoryView(generic.DetailView):
    # song_titles = database.child('Data')
    longtime = 6


def top_short_term_view(request):
    template = "listenInsightsApp/short-term.html"

    top_tracks_short_term = top_tracks['short_term']
    top_artists_short_term = top_artists['short_term']

    track_names = [track[0] for track in top_tracks_short_term]
    track_urls = [track[-1] for track in top_tracks_short_term]
    track_artist_names = [track[1][0] for track in top_tracks_short_term]
    track_artist_urls = [track[1][1] for track in top_tracks_short_term]
    track_album_titles = [track[2] for track in top_tracks_short_term]
    track_album_urls = [track[3] for track in top_tracks_short_term]
    album_release_years = [track[4] for track in top_tracks_short_term]

    artist_names = [artist[0] for artist in top_artists_short_term]
    artist_urls = [artist[-1] for artist in top_artists_short_term]
    artist_genres = [artist[1] for artist in top_artists_short_term]
    artist_popularity_scores = [artist[2] for artist in top_artists_short_term]

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

    return render(request, template, context)


def top_medium_term_view(request):
    template = "listenInsightsApp/medium-term.html"

    top_tracks_medium_term = top_tracks['medium_term']
    top_artists_medium_term = top_artists['medium_term']

    track_names = [track[0] for track in top_tracks_medium_term]
    track_urls = [track[-1] for track in top_tracks_medium_term]
    track_artist_names = [track[1][0] for track in top_tracks_medium_term]
    track_artist_urls = [track[1][1] for track in top_tracks_medium_term]
    track_album_titles = [track[2] for track in top_tracks_medium_term]
    track_album_urls = [track[3] for track in top_tracks_medium_term]
    album_release_years = [track[4] for track in top_tracks_medium_term]

    artist_names = [artist[0] for artist in top_artists_medium_term]
    artist_urls = [artist[-1] for artist in top_artists_medium_term]
    artist_genres = [artist[1] for artist in top_artists_medium_term]
    artist_popularity_scores = [artist[2] for artist in top_artists_medium_term]

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

    return render(request, template, context)


def top_long_term_view(request):
    template = "listenInsightsApp/long-term.html"

    top_tracks_long_term = top_tracks['long_term']
    top_artists_long_term = top_artists['long_term']

    track_names = [track[0] for track in top_tracks_long_term]
    track_urls = [track[-1] for track in top_tracks_long_term]
    track_artist_names = [track[1][0] for track in top_tracks_long_term]
    track_artist_urls = [track[1][1] for track in top_tracks_long_term]
    track_album_titles = [track[2] for track in top_tracks_long_term]
    track_album_urls = [track[3] for track in top_tracks_long_term]
    album_release_years = [track[4] for track in top_tracks_long_term]

    artist_names = [artist[0] for artist in top_artists_long_term]
    artist_urls = [artist[-1] for artist in top_artists_long_term]
    artist_genres = [artist[1] for artist in top_artists_long_term]
    artist_popularity_scores = [artist[2] for artist in top_artists_long_term]

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

    return render(request, template, context)
