from .models import NewsAggre
import requests
from bs4 import BeautifulSoup
from news.models import *
import re

website_link = [
    
    'https://kathmandupost.com/politics',
    'https://kathmandupost.com/sports',
    'https://kathmandupost.com/opinion'
]

def my_corn_job():
    for site in website_link:
        if site == website_link[0]:
            r = requests.get(website_link[0])
            soup = BeautifulSoup(r.content,'html.parser')
            article =soup.find_all('article')
            for content in article[:5]:
                aggre = NewsAggre()
                aggre.news_headline =  content.a.text
                url = content.img["data-src"]
                aggre.image_link = url
                aggre.href_link = "https://kathmandupost.com/politics"+content.a["href"]
                aggre.news_category="P"
                # data = NewsAggre.objects.filter(news_category='P').filter(news_headline =aggre.news_headline)
                aggre.save()
        elif site == website_link[1]:
            r = requests.get(website_link[1])
            soup = BeautifulSoup(r.content,'html.parser')
            article =soup.find_all('article')
            for content in article[:5]:
                aggre = NewsAggre() 
                aggre.news_headline =  content.a.text
                url = content.img["data-src"]
                aggre.image_link = url
                aggre.href_link = "https://kathmandupost.com"+content.a["href"]
                aggre.news_category="H"
                # data = NewsAggre.objects.filter(news_category='S').filter(news_headline =aggre.news_headline)
                aggre.save()
        elif site == website_link[2]:
            r = requests.get(website_link[2])
            soup = BeautifulSoup(r.content,'html.parser')
            article =soup.find_all('article')
            for content in article[:5]:
                aggre = NewsAggre()
                aggre.news_headline =  content.a.text
                url = content.img["data-src"]
                aggre.image_link = url
                aggre.href_link = "https://kathmandupost.com"+content.a["href"]
                aggre.news_category="H"
                # data = NewsAggre.objects.filter(news_category='S').filter(news_headline =aggre.news_headline)
                aggre.save()

