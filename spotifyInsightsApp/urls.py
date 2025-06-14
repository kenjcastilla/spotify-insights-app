from django.urls import path

from . import views

app_name = "spotifyInsightsApp"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("auth-error/", views.auth_error_view, name="auth-error"),
    path("callback", views.spotify_callback, name="callback"),
    path("short-term/", views.top_short_term_view, name="short-term"),
    path("medium-term/", views.top_medium_term_view, name="medium-term"),
    path("long-term/", views.top_long_term_view, name="long-term")
    # path("__debug__/", include("debug_toolbar.urls")),
]
