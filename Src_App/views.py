from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
import os
from datetime import datetime
from pytz import timezone


def Intro(request):
    return render(request, 'intro.html')


def FrancisArtwork(request):
    # Set the time zone to 'US/Eastern'
    eastern = timezone('US/Eastern')

    # Get the current time in the 'US/Eastern' time zone
    now_eastern = datetime.now(eastern)

    # Format today's date
    today = now_eastern.strftime("%B %d, %Y")

    # Generate image path for today
    today_image_path = f'{today}.jpeg'

    context = {
        'today_image_path': today_image_path,
        'today_date': today,
    }

    return render(request, 'francis-artwork.html', context)


def ViewMepkinDailyWord(request):
    mepkin_daily_words = MepkinDailyWord.objects.all()
    bio = Bio.objects.first()

    message = ""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('create-mepkin-daily-word')
        else:
            message = "Invalid username or password."

    context = {
        'mepkin_daily_words': mepkin_daily_words,
        'bio': bio,
        'message': message,
    }

    return render(request, 'mepkin-daily-word.html', context)


@login_required(login_url='mepkin-daily-word')
def CreateMepkinDailyWord(request):
    mepkin_daily_words = MepkinDailyWord.objects.all()
    bio = Bio.objects.first()

    bioMessage = ""
    postMessage = ""

    if request.method == 'POST':
        if 'bioButton' in request.POST:
            bio.content = request.POST.get('content')
            bio.save()
            bioMessage = "Bio updated successfully."

        elif 'postButton' in request.POST:
            MepkinDailyWord.objects.create(post=request.POST.get('post'))
            postMessage = "Post created successfully."

    context = {
        'mepkin_daily_words': mepkin_daily_words,
        'bio': bio,
        'bioMessage': bioMessage,
        'postMessage': postMessage,
    }
    return render(request, 'create-mepkin-daily-word.html', context)


def DeleteMepkinDailyWord(request, pk):
    mepkin_daily_word = MepkinDailyWord.objects.get(id=pk)
    mepkin_daily_word.delete()
    return redirect('create-mepkin-daily-word')


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

        message = ""

        if 'pray' in request.POST:
            Prayer.objects.create(
                name=request.POST.get('name'),
                type=request.POST.get('type'),
                prayer_msg=request.POST.get('prayer_msg'),
            )
            message = """
                Your prayer request has been received and thoughtfully added to Mepkin Abbey’s Prayer List.<br><br>

                “May God grant you your heart’s desire and fulfill all your plans.” - Psalms 20:4.<br>
                We hold you in our prayers, trusting in the Lord’s guidance and comfort for you and your loved ones during this time.<br>
                May you feel His presence and peace more profoundly each day.
            """


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


def DeletePrayerRequest(request, pk):
    prayer_request = Prayer.objects.get(id=pk)
    prayer_request.delete()
    return redirect('prayer-request')


def DeleteGratitudePrayer(request, pk):
    gratitude_prayer = Prayer.objects.get(id=pk)
    gratitude_prayer.delete()
    return redirect('gratitude-prayer')


def Resources(request):
    return render(request, 'resources.html')


def AboutApp(request):
    unique_visitors_count = Visitor.objects.count()
    # return render(request, 'your_template.html', {'unique_visitors_count': unique_visitors_count})
    return render(request, 'about-app.html', {'unique_visitors_count': unique_visitors_count})


def LuceGardens(request):
    base_path = 'static/gallery/Luce Garden/'

    # Filter only image files (you can add more image extensions if needed)
    image_paths = [file for file in os.listdir(base_path) if
                   file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'luce-gardens.html', context)


def MepkinAbbeyChurch(request):
    base_path = 'static/gallery/Mepkin Church/'

    # Filter only image files (you can add more image extensions if needed)
    image_paths = [file for file in os.listdir(base_path) if
                   file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'mepkin-abbey-church.html', context)


def StClaireWalkway(request):
    return render(request, 'st-claire-walkway.html')


def ReceptionCenterOrGiftShop(request):
    return render(request, 'reception-center-or-gift-shop.html')


def MemorialGarden(request):
    return render(request, 'memorial-garden.html')


def CharlestonFirefightersMemorial(request):
    return render(request, 'charleston-firefighters-memorial.html')


def Labyrinth(request):
    base_path = 'static/gallery/Labyrinth/'

    # Filter only image files (you can add more image extensions if needed)
    image_paths = [file for file in os.listdir(base_path) if
                   file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'labyrinth.html', context)


def CrossroadsOrSacredHeartOfJesusStatue(request):
    return render(request, 'crossroads-or-sacred-heart-of-jesus-statue.html')


def MepkinAbbeyBotanicalGarden(request):
    return render(request, 'mepkin-abbey-botanical-garden.html')


def MepkinAbbeyColumbarium(request):
    base_path = 'static/gallery/Columbarium/'

    # Filter only image files (you can add more image extensions if needed)
    image_paths = [file for file in os.listdir(base_path) if
                   file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'mepkin-abbey-columbarium.html', context)


def JohnLaurensGraveOrCemetery(request):
    base_path = 'static/gallery/Laurens Cemetery/'

    # Filter only image files (you can add more image extensions if needed)
    image_paths = [file for file in os.listdir(base_path) if
                   file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'john-laurens-grave-or-cemetery.html', context)


def MeditationGardenOfTruthAndReconciliation(request):
    base_path = 'static/gallery/Meditation Garden/'

    # Filter only image files (you can add more image extensions if needed)
    image_paths = [file for file in os.listdir(base_path) if
                   file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    print(image_paths)

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'meditation-garden-of-truth-and-reconciliation.html', context)


def SacredCorridor(request):
    return render(request, 'sacred-corridor.html')


def AfricanAmericanCemetery(request):
    return render(request, 'african-american-cemetery.html')


def OfficesAndPrivateRooms(request):
    return render(request, 'offices-and-private-rooms.html')


def FlightToEgypt(request):
    base_path = 'static/gallery/Sculptures/'

    # Filter only image files (you can add more image extensions if needed)
    image_paths = [file for file in os.listdir(base_path) if
                   file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    context = {
        'image_paths': image_paths,
    }
    return render(request, 'flight-to-egypt.html', context)


def OurLadyOfMepkin(request):
    base_path = 'static/gallery/Our Lady of Mepkin/'

    # Filter only image files (you can add more image extensions if needed)
    image_paths = [file for file in os.listdir(base_path) if
                   file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'our-lady-of-mepkin.html', context)


def MepkinVideoContent(request):
    return render(request, 'mepkin-video-content.html')

