from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Index),
    path('home/', views.Home, name='home'),
    path('brothers/', views.Brothers, name='brothers'),
    path('gardens/', views.Gardens, name='gardens'),
    path('retreat-center/', views.Retreat, name='retreat'),
    path('who-we-are/', views.WeAre, name='who-we-are'),
    path('grounds-tour/', views.Grounds,name='grounds'),
    path('daily-life/', views.DailyLife),
    path('vacations/', views.Vacations),
    path('pray-with-us/', views.PrayWithUs),
    path('support/', views.Support),
    path('lady-of-mepkin/', views.LadyOfMepkin),
    path('virtual-tour/', views.VirtualTour),
    path('laurens-cemetry/', views.LaurensCemetry),
    path('francis-artwork/', views.Artwork, name='artwork')
]