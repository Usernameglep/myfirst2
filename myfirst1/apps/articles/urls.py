from django.urls import path
from .models import Article, Comment, Alfa_Romeo
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.index, name='index'),
    path('alfa_romeo', views.car_alfa, name='alfa_romeo'),
    path('alfa_romeo_145', views.ar_145, name='alfa_romeo_145'),
    path('news_<int:article_id>/', views.ar_145, name='detail'),
    path('cars_<int:car_id>/', views.car, name='detail'),
]

# Create your views here.