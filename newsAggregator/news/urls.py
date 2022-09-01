from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
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
