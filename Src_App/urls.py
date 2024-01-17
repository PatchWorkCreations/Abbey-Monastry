from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index),

    path('home/', views.Home, name='home'),

    path('virtual-tour/', views.VirtualTour, name='virtual-tour'),
    path('the-gardens/', views.TheGardens, name='the-gardens'),
    path('francis-artwork/', views.FrancisArtwork, name='francis-artwork'),
    path('the-brothers/', views.TheBrothers, name='the-brothers'),
    path('vocation/', views.Vocation, name='vocation'),
    path('retreat-center/', views.RetreatCenter, name='retreat-center'),
    path('news-updates/', views.NewsUpdates, name='news-updates'),

    path('who-we-are/', views.WhoWeAre, name='who-we-are'),
    path('our-daily-life/', views.OurDailyLife, name='our-daily-life'),
    path('pray-with-us/', views.PrayWithUs, name='pray-with-us'),

    path('monastic-prayer/', views.MonasticPrayer, name='monastic-prayer'),

    path('twitter-updates/', views.TwitterUpdates, name='twitter-updates'),

    path('grounds-tour-map/', views.GroundsTourMap, name='grounds-tour-map'),
    path('virtual-tour-street-view/', views.VirtualTourStreetView, name='virtual-tour-street-view'),
    path('prayer-request/', views.PrayerRequests, name="prayer-request"),
    path('prayer-request-list/', views.PrayerRequestList, name="prayer-request-list"),
    path('support/', views.Support, name='support'),

    path('luce-gardens/', views.LuceGardens, name="luce-gardens"),
    path('mepkin-abbey-church/', views.MepkinAbbeyChurch, name="mepkin-abbey-church"),
    path('st-claire-walkway/', views.StClaireWalkway, name="st-claire-walkway"),
    path('reception-center-or-gift-shop/', views.ReceptionCenterOrGiftShop, name="reception-center-or-gift-shop"),
    path('memorial-garden/', views.MemorialGarden, name="memorial-garden"),
    path('charleston-firefighters-memorial/', views.CharlestonFirefightersMemorial,
         name="charleston-firefighters-memorial"),
    path('labyrinth/', views.Labyrinth, name="labyrinth"),
    path('crossroads-or-sacred-heart-of-jesus-statue/', views.CrossroadsOrSacredHeartOfJesusStatue,
         name="crossroads-or-sacred-heart-of-jesus-statue"),
    path('mepkin-abbey-botanical-garden/', views.MepkinAbbeyBotanicalGarden, name="mepkin-abbey-botanical-garden"),
    path('mepkin-abbey-columbarium/', views.MepkinAbbeyColumbarium, name="mepkin-abbey-columbarium"),
    path('john-laurens-grave-or-cemetery/', views.JohnLaurensGraveOrCemetery, name="john-laurens-grave-or-cemetery"),
    path('meditation-garden-of-truth-and-reconciliation/', views.MeditationGardenOfTruthAndReconciliation,
         name="meditation-garden-of-truth-and-reconciliation"),
    path('african-american-cemetery/', views.AfricanAmericanCemetery, name="african-american-cemetery"),
    path('offices-and-private-rooms/', views.OfficesAndPrivateRooms, name="offices-and-private-rooms"),
]
