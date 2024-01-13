from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import PrayerRequest
import os


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
    base_path = '../media/francis-artwork/'

    image_paths = [os.path.join(base_path, f'thumbnail_IMG ({i}).jpeg') for i in range(1, 36)]
    # If you need more paths, adjust the range accordingly

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'francis-artwork.html', context)


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


def TwitterUpdates(request):
    return render(request, 'twitter-updates.html')


def PrayerRequests(request):
    if request.method == 'POST':
        if 'prayer_request' in request.POST:
            PrayerRequest.objects.create(
                name=request.POST.get('name'),
                prayer_request=request.POST.get('prayer_req'),
            )
            message = "Prayer request submitted successfully."

        elif 'admin_login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('prayer-request-list')
            else:
                message = "Invalid username or password."

        return render(request, 'prayer-request.html', {'message': message})

    return render(request, 'prayer-request.html')


@login_required(login_url='prayer-request')
def PrayerRequestList(request):
    prayer_requests = PrayerRequest.objects.all()

    return render(request, 'prayer-request-list.html', {'prayer_requests': prayer_requests})
