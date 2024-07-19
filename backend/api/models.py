# api/models.py
from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='music/')

    def __str__(self):
        return self.title
