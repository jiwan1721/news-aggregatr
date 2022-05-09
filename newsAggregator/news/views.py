from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from news.models import *
import re
from . import cron
# Create your views here.
# r = requests.get("https://ekantipur.com/sports")

# soup = BeautifulSoup(r.content)
# newsdiv = soup.findAll("div",{"class":"teaser offset"})

# ekatpur = []

# for n in newsdiv:
#     print(n.text)



# r1 = requests.get("https://kathmandupost.com/")

# soup1 = BeautifulSoup(r1.content)
# newh2 = soup1.findAll('h2')
# for n in newh2:
#     print(n.text)
r1 = requests.get("https://kathmandupost.com/")
soup1 = BeautifulSoup(r1.content,'html5lib')
newh2 = soup1.find_all('h3')


# newh2 = newh2[0:12]
enews = []
for n1 in newh2:
    enews.append(n1.text)


ekantipur = requests.get("https://ekantipur.com/")
ekantipur_soup = BeautifulSoup(ekantipur.content,'html.parser')
# import ipdb;ipdb.set_trace()
news_ekantpur = ekantipur_soup.find_all('article')
# a_href=ekantipur_soup.find_all("a").get("href")
ekantipur_news = []
all_link = set()
# for n in news_ekantpur:
    # print(news_ekantpur)
    # print(n.h2)
    # link = n.a['href']
    # ekantipur_news.append(n.text)
    
    # all_link.add(link)
    # if(n.get('href')!='#'):
    #     link_text = ("https://ekantipur.com/"+n.get('href'))
    #     all_link.add(link_text)
    #     print(all_link)

# ['https://www.nepalnews.com/s/politics','https://www.nepalnews.com/s/sports','https://www.nepalnews.com/s/business']
url = "https://www.nepalnews.com/s/politics"
request_news= requests.get(url)
html_news = request_news.content
news_soup = BeautifulSoup(html_news,'html.parser')
news_scrap = news_soup.find_all('div',class_ = 'uk-grid-margin uk-first-column')
# for link in news_scrap:
#     aggre = NewsAggre()
#     aggre.news_headline =  link.a.text
#     aggre.news_image = link.img['src']
#     aggre.href_link = link.a['href']
#     aggre.news_category='P'
#     # data = NewsAggre.objects.filter(category='P').filter(news_headline =aggre.news_headline)
#     aggre.save()

r = requests.get("https://kathmandupost.com/")
soup = BeautifulSoup(r.content,'html.parser')
article =soup.find_all('article')
for content in article[:5]:
    aggre = NewsAggre()
    aggre.news_headline =  content.a.text
    url = content.img["data-src"]
    aggre.image_link = url
    aggre.href_link = "https://kathmandupost.com/"+content.a["href"]
    aggre.news_category="P"
    data = NewsAggre.objects.filter(news_category='P').filter(news_headline =aggre.news_headline)
    aggre.save()
 
    # print('href------>',content.a['href'])
    # print('img--->',content.p.text)
    # print('figure---',content.img['data-src'])



def index(request):
    return render(request,'news/index.html',{'e_news':enews,'ekantipur_news':all_link})

# news':news_set