from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
import os
from datetime import datetime
from pytz import timezone
from django.utils import timezone as tz
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt


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
    today_image_path = f'{today}.jpg'

    context = {
        'today_image_path': today_image_path,
        'today_date': today,
    }

    return render(request, 'francis-artwork.html', context)


from django.core.paginator import Paginator

def ViewMepkinDailyWord(request):
    mepkin_daily_words_list = MepkinDailyWord.objects.all()
    paginator = Paginator(mepkin_daily_words_list, 10)  # Show 10 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

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
        'page_obj': page_obj,
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


from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='pray')
def PrayerRequest(request):
    list_of_prayers = Prayer.objects.filter(type="Prayer Request").order_by("-created")
    paginator = Paginator(list_of_prayers, 10)  # Show 10 prayers per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'prayer-request.html', {'page_obj': page_obj})


from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='pray')
def GratitudePrayer(request):
    list_of_prayers = Prayer.objects.filter(type="Gratitude Prayer").order_by("-created")
    paginator = Paginator(list_of_prayers, 10)  # Show 10 prayers per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gratitude-prayer.html', {'page_obj': page_obj})


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
    # Calculate unique visitor count based on distinct session keys
    unique_visitors_count = Visitor.objects.aggregate(unique_visitors=Count('session_key', distinct=True))['unique_visitors']

    # Active visitors in the last 1 minute
    active_threshold = tz.now() - timedelta(minutes=1)
    active_visitors_count = Visitor.objects.filter(last_active__gte=active_threshold).count()

    return render(request, 'about-app.html', {
        'unique_visitors_count': unique_visitors_count,
        'active_visitors_count': active_visitors_count,
    })


def get_active_visitors(request):
    active_threshold = tz.now() - timedelta(minutes=1)  # Match your polling interval
    active_visitors_count = Visitor.objects.filter(last_active__gte=active_threshold).count()
    return JsonResponse({"active_visitors_count": active_visitors_count})


@csrf_exempt
def update_activity(request):
    if request.method == 'POST':
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key
        ip_address = request.META.get('REMOTE_ADDR', '')

        Visitor.objects.update_or_create(
            session_key=session_key,
            defaults={'last_active': tz.now(), 'ip_address': ip_address}
        )
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)


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

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'meditation-garden-of-truth-and-reconciliation.html', context)


def SacredCorridor(request):
    base_path = 'static/gallery/Sacred Corridor/'

    # Filter only image files (you can add more image extensions if needed)
    image_paths = [file for file in os.listdir(base_path) if
                   file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    context = {
        'image_paths': image_paths,
    }

    return render(request, 'sacred-corridor.html', context)


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

def Mepkinabbeyfacebook(request):
    return render(request, 'mepkinabbeyfacebook.html')

# Src_App/views.py

import os
from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator

def gallery(request):
    gallery_path = os.path.join(settings.BASE_DIR, 'static/gallery/Francis Artwork')
    images = []

    for filename in os.listdir(gallery_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            images.append(f'gallery/Francis Artwork/{filename}')

    paginator = Paginator(images, 9)  # Show 9 images per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery.html', {'page_obj': page_obj})

def accesibility(request):
    return render(request, 'accesibility.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from django.conf import settings
from datetime import datetime
from pytz import timezone

@login_required
def admin_dashboard(request):
    # Set the time zone to 'US/Eastern'
    eastern = timezone('US/Eastern')

    # Get the current time in the 'US/Eastern' time zone
    now_eastern = datetime.now(eastern)

    artwork_path = os.path.join(settings.BASE_DIR, 'static/gallery/Francis Artwork')
    photos = [f for f in os.listdir(artwork_path) if os.path.isfile(os.path.join(artwork_path, f)) and f.endswith(('.jpg', '.jpeg', '.png'))]

    # Filter photos with future dates
    future_photos = []
    for photo in photos:
        try:
            photo_date = datetime.strptime(photo.split('.')[0], "%B %d, %Y")
            photo_date = eastern.localize(photo_date)  # Make the datetime timezone-aware
            if photo_date > now_eastern:
                future_photos.append(photo)
        except ValueError:
            # Handle the case where the filename doesn't match the expected date format
            pass

    if len(future_photos) <= 3:
        messages.warning(request, 'Only 3 or fewer future photos are left in the Francis Artwork section. Please upload more photos.')

    return render(request, 'admin_dashboard/admin_dashboard.html', {'photos_left': len(future_photos)})

@login_required
def admin_edit(request):
    if request.method == 'POST':
        # Handle the form submission
        pass
    return render(request, 'admin_dashboard/edit.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Ensure this import is present
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from datetime import datetime, timedelta
from pytz import timezone

@login_required
def upload_photos(request):
    if request.method == 'POST':
        section = request.POST.get('section')
        start_date = request.POST.get('start_date')
        num_days = int(request.POST.get('num_days'))
        files = request.FILES.getlist('photos')  # Ensure this matches the form field name

        if section == 'francis_artwork':
            fs = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'static/gallery/Francis Artwork'))
            eastern = timezone('US/Eastern')
            start_date = datetime.strptime(start_date, "%Y-%m-%d").replace(tzinfo=eastern)

            for i, file in enumerate(files):
                if i < num_days:
                    current_date = start_date + timedelta(days=i)
                    current_date_str = current_date.strftime("%B %d, %Y")
                    filename = fs.save(current_date_str + '.jpg', file)
                else:
                    break

            messages.success(request, 'Photos uploaded successfully for Francis Artwork.')

        # Add handling for other sections as needed

        return redirect('admin_dashboard')

    return render(request, 'admin_dashboard/upload_photo.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from datetime import datetime
from pytz import timezone

@login_required
def upload_francis_artwork(request):
    if request.method == 'POST' and request.FILES['photo']:
        artwork = request.FILES['photo']
        fs = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'static/gallery/Francis Artwork'))
        
        # Set the time zone to 'US/Eastern'
        eastern = timezone('US/Eastern')

        # Get the current time in the 'US/Eastern' time zone
        now_eastern = datetime.now(eastern)

        # Format today's date
        today_date = now_eastern.strftime("%B %d, %Y")

        # Use today's date as the file name
        filename = fs.save(today_date + '.jpg', artwork)
        
        return redirect('admin_dashboard')
    
    return render(request, 'admin_dashboard/upload_photo.html')
