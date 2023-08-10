from django.urls import include, path

from . import views

app_name = "listenInsightsApp"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("short-term/", views.top_short_term_view, name="short-term"),
    path("medium-term/", views.top_medium_term_view, name="medium-term"),
    path("long-term/", views.top_long_term_view, name="long-term")
    # path("__debug__/", include("debug_toolbar.urls")),
]
