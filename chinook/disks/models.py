from django.db import models

# Create your models here.
class Artist(models.Model):
    id = models.IntegerField
    name = models.CharField

class Album(models.Model):
    id = models.IntegerField
    title = models.CharField
    artist = models.ForeignKey(Artist)
    
class Track(models.Model):
    id = models.IntegerField
    name = models.CharField
    composer = models.CharField
    milliseconds = models.IntegerField
    bytes = models.IntegerField
    unitPrice = models.FloatField
    album = models.ForeignKey(Album)
    

    
