from django.db import models

class Intro(models.Model):
    img = models.ImageField()
    text = models.TextField()
