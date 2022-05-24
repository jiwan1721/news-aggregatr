from django.urls import path,include,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
# from .views import api_root
# from django.views.generic.base import RedirectView
app_name = 'news'

# router = DefaultRouter()
# router.register(r'newslist', views.NewsList,basename='news-list')







urlpatterns = [
    # path('rou/',include(router.urls)),    




    path('v1',views.NewsList.as_view(), name = 'news_info'),
    path('v1/<int:pk>',views.NewsUpdate.as_view()),

    path('index',views.index,name ="index"),
    path("register/", views.register_request, name="register"),
    path("", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("politics",views.politics_news,name ="politics"),
    path('sports',views.sports_news,name = 'sports'),
    path('health',views.health_news,name = 'health'),
    path('search',views.search,name = 'search'),
    path('search-authentication',views.exampleView.as_view(),name ='example-view'),

    path('api_root',views.api_root)
    
   
    
    
]
# urlpatterns = [
#     path('',include(router.urls)),
#     path('api-auth',include('rest_framework.urls')),
# ]