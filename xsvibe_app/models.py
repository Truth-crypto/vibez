from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.

class Music(models.Model):
    musicname = models.CharField(max_length=200)
    artistname = models.CharField(max_length=200)
    file = models.FileField(upload_to='music')
    musicimg = models.ImageField(upload_to='image')
    created = models.TimeField(default=datetime.now())
    

    

    def __str__(self):
        return f'{self.musicname}-{self.artistname}--{self.file}'

class Video(models.Model):
    videoname = models.CharField(max_length=200)
    videotitle = models.CharField(max_length=200)
    video = models.FileField(upload_to='video')
    videoimg = models.ImageField(upload_to='image')
    created = models.TimeField(default=datetime.now())
    

    

    def __str__(self):
        return f'{self.videoname}-{self.videotitle}--{self.created}'


class Ads(models.Model):
    adsname = models.CharField(max_length=300)
    adsdescription = models.TextField(default='')
    adsimg = models.ImageField(upload_to='image')
    adslink = models.CharField(max_length=300)
    
    def __str__(self):
            return f'{self.adsname}-{self.adsimg}'

class FreeBeat(models.Model):
    beatname = models.CharField(max_length=200)
    beatartistname = models.CharField(max_length=230)
    beatfile = models.FileField(upload_to='music')
    beatimg = models.ImageField(upload_to='image')
    created = models.TimeField(default=datetime.now())



    def __str__(self):
        return f'{self.beatname}-{self.beatfile}--{self.beatimg}'

