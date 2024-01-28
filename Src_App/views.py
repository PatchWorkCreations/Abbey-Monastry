from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Prayer
import os


def FrancisArtwork(request):
    base_path = '../static/francis-artwork/'

    image_paths = [os.path.join(base_path, f'thumbnail_IMG ({i}).jpg') for i in range(1, 36)]
    # If you need more paths, adjust the range accordingly

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'francis-artwork.html', context)


def Index(request):
    return render(request, 'index.html')


def Home(request):
    return render(request, 'home.html')


def VirtualTour(request):
    return render(request, 'virtual-tour.html')


def TheGardens(request):
    return render(request, 'the-gardens.html')


def TheBrothers(request):
    return render(request, 'the-brothers.html')


def Vocation(request):
    return render(request, 'vocation.html')


def RetreatCenter(request):
    return render(request, 'retreat-center.html')


def NewsUpdates(request):
    return render(request, 'news-updates.html')


def PrayWithUs(request):
    return render(request, 'pray-with-us.html')


def WhoWeAre(request):
    return render(request, 'who-we-are.html')


def OurDailyLife(request):
    return render(request, 'our-daily-life.html')


def TwitterUpdates(request):
    return render(request, 'twitter-updates.html')


def MonasticPrayer(request):
    return render(request, 'monastic-prayer.html')


def GroundsTourMap(request):
    return render(request, 'grounds-tour-map.html')


def VirtualTourStreetView(request):
    return render(request, 'virtual-tour-street-view.html')


def Pray(request):
    if request.method == 'POST':
        if 'pray' in request.POST:
            Prayer.objects.create(
                name=request.POST.get('name'),
                type=request.POST.get('type'),
                prayer_msg=request.POST.get('prayer_msg'),
            )
            message = "Request submitted successfully."

        elif 'admin_login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('list-of-prayers')
            else:
                message = "Invalid username or password."

        return render(request, 'pray.html', {'message': message})

    return render(request, 'pray.html')


@login_required(login_url='pray')
def ListOfPrayers(request):
    return render(request, 'list-of-prayers.html')


def Support(request):
    return render(request, 'support.html')


def Connect(request):
    return render(request, 'connect.html')


@login_required(login_url='pray')
def PrayerRequest(request):
    list_of_prayers = Prayer.objects.all()

    return render(request, 'prayer-request.html', {'list_of_prayers': list_of_prayers})


@login_required(login_url='pray')
def GratitudePrayer(request):
    list_of_prayers = Prayer.objects.all()

    return render(request, 'gratitude-prayer.html', {'list_of_prayers': list_of_prayers})


def LuceGardens(request):
    base_path = '../static/luce-gardens-images/'

    image_paths = [os.path.join(base_path, f'luce gardens ({i}).jpg') for i in range(1, 15)]
    # If you need more paths, adjust the range accordingly

    print(image_paths)

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'luce-gardens.html', context)


def MepkinAbbeyChurch(request):
    return render(request, 'mepkin-abbey-church.html')


def StClaireWalkway(request):
    return render(request, 'st-claire-walkway.html')


def ReceptionCenterOrGiftShop(request):
    return render(request, 'reception-center-or-gift-shop.html')


def MemorialGarden(request):
    return render(request, 'memorial-garden.html')


def CharlestonFirefightersMemorial(request):
    return render(request, 'charleston-firefighters-memorial.html')


def Labyrinth(request):
    return render(request, 'labyrinth.html')


def CrossroadsOrSacredHeartOfJesusStatue(request):
    return render(request, 'crossroads-or-sacred-heart-of-jesus-statue.html')


def MepkinAbbeyBotanicalGarden(request):
    return render(request, 'mepkin-abbey-botanical-garden.html')


def MepkinAbbeyColumbarium(request):
    return render(request, 'mepkin-abbey-columbarium.html')


def JohnLaurensGraveOrCemetery(request):
    return render(request, 'john-laurens-grave-or-cemetery.html')


def MeditationGardenOfTruthAndReconciliation(request):
    return render(request, 'meditation-garden-of-truth-and-reconciliation.html')


def SacredCorridor(request):
    return render(request, 'sacred-corridor.html')


def AfricanAmericanCemetery(request):
    return render(request, 'african-american-cemetery.html')


def OfficesAndPrivateRooms(request):
    return render(request, 'offices-and-private-rooms.html')


def FlightToEgypt(request):
    return render(request, 'flight-to-egypt.html')
