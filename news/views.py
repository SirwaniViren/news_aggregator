from django.shortcuts import render, redirect
from bs4 import BeautifulSoup 
from news.models import Article
import requests

# Create your views here.
def getArticle(request):
    url = "https://www.bbc.com/"
    headers = { "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')

    articles = soup.find_all('li', class_=lambda value: value and value.startswith('media-list__item media-list__item'))
    for article in articles:
        pass 