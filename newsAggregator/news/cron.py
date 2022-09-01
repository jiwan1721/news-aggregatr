
import requests
from bs4 import BeautifulSoup
from news.aggregator import *
import re
from urllib.parse import urlparse
from . import utils
website_link = [
    'https://kathmandupost.com/politics',
    'https://kathmandupost.com/sports',
    'https://kathmandupost.com/opinion',
]
ekantipur = [
    'https://ekantipur.com/opinion',
    'https://ekantipur.com/sports',
    'https://ekantipur.com/health',
    ]
himalayan = [
    'https://thehimalayantimes.com/business',
    'https://thehimalayantimes.com/sports',
    'https://thehimalayantimes.com/opinion',
]
def my_corn_job():
    for site in website_link:
        r = requests.get(site)
        soup = BeautifulSoup(r.content,'html.parser')
        article =soup.find_all('article')
        url_host = utils.get_host_name(site)
        url_parse = urlparse(site)
        for content in article[:5]:
            aggre = NewsAggre()
            aggre.news_headline =  content.h3.text
            aggre.news_descriptions = content.p.text
            url = content.img["data-src"]
            aggre.image_link = url
            aggre.href_link = url_host +content.a["href"]
            if url_parse.path == '/politics':
                aggre.news_category="P"
            elif url_parse.path =='/sports':
                aggre.news_category="S"
            elif url_parse.path =='/opinion':
                aggre.news_category="O"
            else:
                aggre.news_category="R"
            if not NewsAggre.objects.filter(href_link=aggre.href_link).exists(): 
                aggre.save()    
            # data = NewsAggre.objects.filter(news_headline =aggre.news_headline)
            
            

for site in ekantipur:
    r = requests.get(site)
    soup = BeautifulSoup(r.content,'html.parser')
    article =soup.find_all('article')
    url_host = utils.get_host_name(site)
    url_parse = urlparse(site)
    for content in article[:5]:
        aggre = NewsAggre()
        aggre.news_headline =  content.a.text
        aggre.news_descriptions = content.p.text
        url = content.img["data-src"]
        aggre.image_link = url
        aggre.href_link = url_host +content.a["href"]
        if url_parse.path == '/opinion':
            aggre.news_category="P"
        elif url_parse.path =='/sports':
            aggre.news_category="S"
        elif url_parse.path =='/health':
            aggre.news_category="H"
        else:
            aggre.news_category="R"
        if not NewsAggre.objects.filter(href_link=aggre.href_link).exists(): 
                aggre.save()
    
    for site in himalayan:
            r = requests.get(site)
            soup = BeautifulSoup(r.content,'html.parser')
            article =soup.find_all('article')
            url_host = utils.get_host_name(site)
            url_parse = urlparse(site)
            for content in article[:5]:
                aggre = NewsAggre()
                aggre.news_headline =  content.h3.text
                # aggre.news_descriptions = content.p.text
                url = content.img["data-src"]
                aggre.image_link = url
                aggre.href_link = content.a["href"]
                if url_parse.path == '/opinion':
                    aggre.news_category="P"
                elif url_parse.path =='/sports':
                    aggre.news_category="S"
                elif url_parse.path =='/health':
                    aggre.news_category="H"
                else:
                    aggre.news_category="R"  
                if not NewsAggre.objects.filter(href_link=aggre.href_link).exists(): 
                    aggre.save()              
    

# def delete_duplicate():
#     for row in NewsAggre.objects.all().reverse():
#         if NewsAggre.objects.filter(news_headline=row.news_headline).count()>1:
#             row.delete()