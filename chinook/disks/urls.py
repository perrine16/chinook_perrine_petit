from django.urls import path
from . import views

app_name="disks"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:album_id>/", views.detail, name="detail"),
    path("<int:album_id/artist/", views.artist, name="artist"),
    path("<int:album_id>/track/", views.tracklist, name = "tracklist"),
]