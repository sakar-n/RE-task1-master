from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()





# class Squad(models.Model):

    # name = models.CharField(max_length=100)
    # img = models.ImageField(upload_to='pics')
   #  desc = models.TextField()




from django.db import models

# Create your models here.
