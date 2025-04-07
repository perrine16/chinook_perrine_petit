from django.db import models

# Create your models here.
class artist(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name

class album(models.Model):
    artist = models.ForeignKey(artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.artist
    
class track(models.Model):
    album = models.ForeignKey(album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    composer = models.CharField(max_length=200, null=True, blank = True)
    milliseconds = models.IntegerField(default=0)
    bytes = models.IntegerField(default=0)
    unitPrice = models.FloatField(default=0)
    def __str__(self):
        return self.album

    
