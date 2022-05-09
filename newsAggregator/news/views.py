from unicodedata import category
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from news.models import *
import re
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
newh2 = soup1.findAll('h3')
# newh2 = newh2[0:12]
enews = []
for n1 in newh2:
    enews.append(n1.text)


ekantipur = requests.get("https://ekantipur.com/")
ekantipur_soup = BeautifulSoup(ekantipur.content,'html.parser')
news_ekantpur = ekantipur_soup.find_all('h1')
# a_href=ekantipur_soup.find_all("a").get("href")
ekantipur_news = []
all_link = set()
for n in news_ekantpur:
    link = n.get('href')
    ekantipur_news.append(n.text)
    
    all_link.add(link)
    print(all_link)
    # if(n.get('href')!='#'):
    #     link_text = ("https://ekantipur.com/"+n.get('href'))
    #     all_link.add(link_text)
    #     print(all_link)

# ['https://www.nepalnews.com/s/politics','https://www.nepalnews.com/s/sports','https://www.nepalnews.com/s/business']
url = "https://www.nepalnews.com/s/politics"
request_news= requests.get(url)
html_news = request_news.content
news_soup = BeautifulSoup(html_news,'html.parser')
news_scrap = news_soup.find_all('div',{'class':'uk-first-column'})[0:10]
for link in news_scrap:
    aggre = NewsAggre()
    aggre.news_headline =  link.findChildren()[7].text
    aggre.news_image = link.findChildren()[5].get('src')
    aggre.href_link = link.findChildren()[4].get('href')
    aggre.news_category='P'
    data = NewsAggre.objects.filter(category='P').filter(news_headline =aggre.news_headline)
    if len(data)==0:
        aggre.save()
    print(link.findChildren()[5].text)


def index(request):
    return render(request,'news/index.html',{'e_news':enews,'ekantipur_news':all_link})

# news':news_set