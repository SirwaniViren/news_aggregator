from django.shortcuts import render, redirect
from bs4 import BeautifulSoup 
from news.models import Article
import requests
import re


requests.packages.urllib3.disable_warnings()
# Create your views here.
def getArticle(request):
    url = "https://www.bbc.com/"
    headers = { "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')

    articles = soup.find_all('li', class_=re.compile('^media-list__item media-list__item'))
    for piece in articles:
        new_piece = Article()
        if piece.find('a',{'class':'media__link'}) is not None:
            new_piece.title = piece.find('a',{'class':'media__link'}).get_text()
            link_url = piece.find('a',{'class':'media__link'})['href']
            if link_url.startswith('https'):
                new_piece.title_url = str(piece.find('a',{'class':'media__link'})['href'])
            else:
                new_piece.title_url = url + str(piece.find('a',{'class':'media__link'})['href'])
            image = piece.find('img')['src']
            if image is not None:
                new_piece.image = str(image)
            else:
                new_piece.image = 'https://martialartsplusinc.com/wp-content/uploads/2017/04/default-image-620x600.jpg'
            summary = piece.find('p',{'class':'media__summary'})
            if summary is None:
                new_piece.summary = "no summary"
            else:
                new_piece.summary = summary.get_text()
            tag = piece.find('a',{'class':'media__tag tag tag--news'})
            if tag is not None:
                new_piece.tag = tag.get_text()
            else:
                new_piece.tag = "N/A"
        new_piece.save()
    return redirect("../")


def listArticle(request):
    articles = Article.objects.all()[::-1]
    context = {
        'article_list': articles,
    }
    return render(request, "news/index.html", context)