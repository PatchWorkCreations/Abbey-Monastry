from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index),
    path('home/', views.Home, name='home'),
    path('brothers/', views.Brothers, name='brothers'),
    path('gardens/', views.Gardens, name='gardens'),
    path('retreat-center/', views.Retreat, name='retreat'),
    path('who-we-are/', views.WeAre, name='who-we-are'),
    path('grounds-tour/', views.Grounds, name='grounds'),
    path('daily-life/', views.DailyLife),
    path('francis-artwork/', views.FrancisArtwork),
    path('vocation/', views.Vocation),
    path('pray-with-us/', views.PrayWithUs),
    path('support/', views.Support),
    path('virtual-tour/', views.VirtualTour),
    path('virtual-tour-page/', views.VirtualTourPage, name='virtual-tour-page'),
    path('columbarium/', views.Columbarium, name='columbarium'),
    path('monastic-prayer/', views.MonasticPrayer),
    path('news-update/', views.NewsUpdate),
]
