from django.urls import path
from . import views
# from django.views.generic.base import RedirectView
from django.urls import re_path
app_name = 'news'

from django.urls import include
urlpatterns= [
    # re_path(r'^.*$', RedirectView.as_view(url='login', permanent=True), name='index'),
    path('index',views.index,name ="index"),
    path("register/", views.register_request, name="register"),
    path("", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("politics",views.politics_news,name ="politics"),
    path('sports',views.sports_news,name = 'sports'),
    path('health',views.health_news,name = 'health'),
    path('search',views.search,name = 'search'),
    path('api/v1',views.NewsList.as_view()),
    path('api/v1/<int:pk>',views.NewsUpdate.as_view()),
    path('api-auth',include('rest_framework.urls')),
    
]