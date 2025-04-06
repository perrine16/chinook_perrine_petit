from django.db import models

# Create your models here.
class artist(models.Model):
    name = models.CharField(max_length=200)

class album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(artist, on_delete=models.CASCADE)
    
class track(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    milliseconds = models.IntegerField(default=0)
    bytes = models.IntegerField(default=0)
    unitPrice = models.FloatField(default=0)
    album = models.ForeignKey(album, on_delete=models.CASCADE)

    
