from django.urls import path
from . import views
app_name = 'news'

urlpatterns= [
    path('',views.index,name ="index"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("politics",views.politics_news,name ="politics"),
    path('sports',views.sports_news,name = 'sports'),
    path('health',views.health_news,name = 'health'),
    path('search',views.search,name = 'search'),
]