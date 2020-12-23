from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    url = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    albums = models.ManyToManyField('Album')

class Album(models.Model):
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
