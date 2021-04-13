from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True,blank=True)
    title_url = models.TextField
    summary = models.CharField(max_length=1000,null=True,blank=True)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.title