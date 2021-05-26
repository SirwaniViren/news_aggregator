from django.shortcuts import render, redirect
from bs4 import BeautifulSoup 
from news.models import Article
import requests
import re
import pandas as pd


requests.packages.urllib3.disable_warnings()
# Create your views here.
def scrape():
    titles = []
    urls = []
    images = []
    tags = []
    summaries = []
    url = "https://www.bbc.com"
    headers = { "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')

    articles = soup.find_all('li', class_=re.compile('^media-list__item media-list__item'))
    for piece in articles:
        if piece.find('a',{'class':'media__link'}) is not None:
            titles.append(piece.find('a',{'class':'media__link'}).get_text().strip())
            link_url = piece.find('a',{'class':'media__link'})['href']
            if link_url.startswith('https'):
                urls.append(str(piece.find('a',{'class':'media__link'})['href']))
            else:
                urls.append(url + str(piece.find('a',{'class':'media__link'})['href']))
            image = piece.find('img')['src']
            if image is not None and not image.startswith("data"):
                images.append(str(image))
            else:
                images.append('https://martialartsplusinc.com/wp-content/uploads/2017/04/default-image-620x600.jpg')
            summary = piece.find('p',{'class':'media__summary'})
            if summary is None:
                summaries.append("no summary")
            else:
                summaries.append(summary.get_text().strip())
            tag = piece.find('a',{'class':'media__tag tag tag--news'})
            if tag is not None:
                tags.append(tag.get_text().strip())
            else:
                tags.append("N/A")
                
    bbc_frame = pd.DataFrame({"title":titles, "url":urls, "image":images,"summary":summaries,"tag":tags})
    return bbc_frame

def getArticle():
    frame = scrape()
    for i in range(len(frame)):
        new_piece = Article()
        new_piece.title = str(frame.loc[i][0])
        new_piece.title_url = frame.loc[i][1]
        new_piece.image = str(frame.loc[i][2])
        new_piece.save()
    return redirect("../")


def listArticle(request):
    articles = Article.objects.all()[::-1]
    context = {
        'article_list': articles,
    }
    return render(request, "news/index.html", context)