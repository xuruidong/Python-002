from django.db import models

# Create your models here.
class DoubanShort(models.Model):
    short = models.CharField(max_length=400)
    stars = models.CharField(max_length=5)
    date = models.DateField("Date", auto_now=True)