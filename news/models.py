from django.db import models
from django.conf import settings

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True,blank=True)
    title_url = models.URLField(null=True,blank=True)
    summary = models.CharField(max_length=1000,null=True,blank=True)
    tag = models.CharField(max_length=100)

    class Meta:
        unique_together = ["title", "image", "title_url","summary", "tag"]

    def __str__(self):
        return self.title