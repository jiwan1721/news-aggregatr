from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from news.aggregator import *
from .form import NewUserForm
import re
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import cron
from . import utils
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

r = requests.get("https://kathmandupost.com/politics")
soup = BeautifulSoup(r.content,'html.parser')
article =soup.find_all('article')
url_host = utils.get_host_name("https://kathmandupost.com/politics")
# for content in article[:5]:
#     aggre = NewsAggre()
#     aggre.news_headline =  content.h3.text
#     url = content.img["data-src"]
#     aggre.image_link = url
    
#     aggre.href_link = url_host + content.a["href"]
#     aggre.news_category="P"
#     data = NewsAggre.objects.filter(news_category='P').filter(news_headline =aggre.news_headline)
#     aggre.save()
 
    # print('href------>',content.a['href'])
    # print('img--->',content.p.text)
    # print('figure---',content.img['data-src'])





# news':news_set

from .form import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="news/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="news/login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("main:homepage")

def index(request):
    data_politics = NewsAggre.objects.all().filter(news_category="P")
    data_health = NewsAggre.objects.all().filter(news_category="H")
    data_sports = NewsAggre.objects.all().filter(news_category="S")
    return render(request,'news/index.html',{
        'politics':data_politics,
        'health':data_health,
        'sports': data_sports
                                             
        })

def politics_news(request):
    data = NewsAggre.objects.all().filter(news_category="P")
    
    return render(request, "news/political.html",{'political_news':data})

def sports_news(request):
    data = NewsAggre.objects.all().filter(news_category="S")
    return render(request, "news/sports.html",{'sports_news':data})

def health_news(request):
    data = NewsAggre.objects.all().filter(news_category="H")
    return render(request, 'news/health.html',{'health_news':data})