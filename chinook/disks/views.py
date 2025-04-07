from django.shortcuts import render, get_object_or_404
from .models import album
# Create your views here.

def index(request):
    album_list = album.objects.order_by("-title")
    context = {
        "album_list" : album_list,
    }
    return render(request, "disks/index.html", context)

def detail(request, album_id):
    a = get_object_or_404(album, pk = album_id)
    return render(request, "disks/detail.html", {"album":a})

def artist(request, album_id):
    a = get_object_or_404(album, pk=album_id)
    return render(request, "disks/artist.html", {"album" : a})

def tracklist(request, album_id):
    a = get_object_or_404(album, pk=album_id)
    return render(request, "disks/tracklist.html", {"album" : a})