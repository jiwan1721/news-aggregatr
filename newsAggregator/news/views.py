from django.shortcuts import render,redirect
from news.aggregator import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .form import NewUserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.db.models import Q
from .serializers import NewsAggreSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("news:login")
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
				return redirect("news:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="news/login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("news:login")

@login_required
def index(request):
    data_politics = NewsAggre.objects.all().filter(news_category="P").order_by('id')[:6]
    data_health = NewsAggre.objects.all().filter(news_category="H").order_by('id')[:6]
    data_sports = NewsAggre.objects.all().filter(news_category="S").order_by('id')[:6]
    context = {
        'politics':data_politics,
        'health':data_health,
        'sports': data_sports
                                             
        }
    return render(request,'news/index.html',context)
@login_required
def politics_news(request):
    data = NewsAggre.objects.all().filter(news_category="P").order_by('id')[:12]
    
    return render(request, "news/political.html",{'political_news':data})
@login_required
def sports_news(request):
    data = NewsAggre.objects.all().filter(news_category="S").order_by('id')[:12]
    return render(request, "news/sports.html",{'sports_news':data})
@login_required
def health_news(request):
    data = NewsAggre.objects.all().filter(news_category="H").order_by('id')[:12]
    return render(request, 'news/health.html',{'health_news':data})

@login_required
def search(request):
    results=[]
    if request.method == "POST":
        searched_text = request.POST.get('search')
        results = NewsAggre.objects.all().filter(
            Q(news_category=searched_text)
            |Q(news_headline__icontains=searched_text)
            |Q(href_link__icontains=searched_text)
            |Q(news_descriptions__icontains=searched_text)
       ).order_by('id')[:12]
    return render(
            request,
            'news/search.html',
            {
            'results': results
            }
        )

class NewsList(generics.ListCreateAPIView):
    queryset = NewsAggre.objects.all()
    serializer_class = NewsAggreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['news_headline']
    def get_object(self):
        obj = get_object_or_404(self.get_queryset(),pk = self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        self.check_object_permissions(self.request, self.filter_backends)
        self.check_object_permissions(self.request, self.search_fields)

        return obj
    def has_object_permission(self,request,view,obj):
        if request.methode in permissions.SAFE_METHODS:
            return True
        return object.NewsAggre == request.user
    
# class NewsList(viewsets.ModelViewSet):
#     queryset = NewsAggre.objects.all()
#     serializer_class = NewsAggreSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['news_headline']
#     def get_object(self):
#         obj = get_object_or_404(self.get_queryset(),pk = self.kwargs["pk"])
#         self.check_object_permissions(self.request, obj)
#         return obj

class NewsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsAggre.objects.all()
    serializer_class = NewsAggreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


#for @rendere_classes we have to import in decorators
@api_view(['GET'])
@renderer_classes([JSONRenderer,BrowsableAPIRenderer])
def api_root(request,format=None):
    return Response({
        'news-aggregator':reverse('news:news_info',request=request,format=None),
        'newsAuthExample':reverse('news:example-view',request=request,format=None),
    })

class exampleView(APIView):
    authentication_classes = [SessionAuthentication,BaseAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        content = {
            'user':str(request.user),
            'auth':str(request.auth), 
        }
        return Response(content)