from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as bs
from news.models import Article
import requests

# Create your views here.
def scrape(request):
    pass