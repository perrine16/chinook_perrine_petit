from django.db import models

# Create your models here.
class artist(models.Model):
    id = models.IntegerField
    name = models.CharField

class album(models.Model):
    id = models.IntegerField
    title = models.CharField
    artist = models.ForeignKey(artist)
    
class track(models.Model):
    id = models.IntegerField
    name = models.CharField
    composer = models.CharField
    milliseconds = models.IntegerField
    bytes = models.IntegerField
    unitPrice = models.FloatField
    album = models.ForeignKey(album)
    

    
