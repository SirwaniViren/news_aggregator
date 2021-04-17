from django.urls import path
from news.views import getArticle, listArticle

urlpatterns = [
  path('getArticle/', getArticle, name="getArticle"),
  path('', listArticle, name="index"),
]