from django.db import models

class short_urls(models.Model):
    short_url = models.CharField(max_length=300)
    long_url = models.CharField("URL", unique=True, max_length=500)


