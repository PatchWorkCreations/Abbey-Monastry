from django.shortcuts import render


def Index(request):
    return render(request, 'index.html')


def Home(request):
    return render(request, 'home.html')


def Brothers(request):
    return render(request, 'brothers.html')


def Gardens(request):
    return render(request, 'gardens.html')


def Retreat(request):
    return render(request, 'retreat.html')


def WeAre(request):
    return render(request, 'who-we-are.html')


def Grounds(request):
    return render(request, 'grounds-tour.html')


def DailyLife(request):
    return render(request, 'daily-life.html')


def Vocation(request):
    return render(request, 'vocation.html')


def PrayWithUs(request):
    return render(request, 'pray-with-us.html')


def FrancisArtwork(request):
    return render(request, 'francis-artwork.html')


def Support(request):
    return render(request, 'support.html')


def VirtualTourPage(request):
    return render(request, 'virtual-tour-page.html')


def VirtualTour(request):
    return render(request, 'virtual-tour.html')


def Columbarium(request):
    return render(request, 'columbarium.html')


def MonasticPrayer(request):
    return render(request, 'monastic-prayer.html')


def NewsUpdate(request):
    return render(request, 'news-update.html')
