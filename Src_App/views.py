from django.shortcuts import render
from .models import *


def Index(request):
    context = {}

    images = Image.objects.all()

    if images:
        images = images[0]
        context['image'] = images

    return render(request, 'index.html', context)


def Home(request):
    context = {}

    images = Image.objects.all()

    if images:
        images = images[0]
        context['image'] = images

    return render(request, 'home.html', context)


def Brothers(request):
    context = {}

    images = Image.objects.all()

    if images:
        images = images[0]
        context['image'] = images

    return render(request, 'brothers.html', context)


def Gardens(request):
    context = {}

    images = Image.objects.all()

    if images:
        images = images[0]
        context['image'] = images

    return render(request, 'gardens.html', context)


def Retreat(request):
    context = {}

    images = Image.objects.all()

    if images:
        images = images[0]
        context['image'] = images

    return render(request, 'retreat.html', context)


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


def Support(request):
    return render(request, 'support.html')


def VirtualTourPage(request):
    return render(request, 'virtual-tour-page.html')


def LadyOfMepkin(request):
    context = {}

    texts = Text.objects.all()

    if texts:
        texts = texts[0]
        context['text'] = texts
    return render(request, 'lady-of-mepkin.html', context)


def VirtualTour(request):
    return render(request, 'virtual-tour.html')


def Columbarium(request):
    return render(request, 'columbarium.html')


def LaurensCemetry(request):
    context = {}

    texts = Text.objects.all()

    if texts:
        texts = texts[0]
        context['text'] = texts
    return render(request, 'laurens-cemetry.html', context)


def Artwork(request):
    artworks = ArtWork.objects.all()

    return render(request, 'artwork.html', {'artworks': artworks})
