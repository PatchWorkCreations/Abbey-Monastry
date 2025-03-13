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

def calling(request):
    return render(request, 'calling.html')


from django.shortcuts import render
from django.utils.timezone import now
from .models import Artwork

def FrancisArtwork(request):
    today_date = now().date()

    # Fetch today's Francis Artwork
    artwork = Artwork.objects.filter(category="francis_artwork", date_uploaded__date=today_date).first()

    # Ensure the correct file extension (.jpg)
    today_image_path_1 = f"{artwork.image1.url}.jpg" if artwork and artwork.image1 else None
    today_image_path_2 = f"{artwork.image2.url}.jpg" if artwork and artwork.image2 else None

    context = {
        "today_image_path_1": today_image_path_1,
        "today_image_path_2": today_image_path_2,
        "today_date": today_date.strftime("%B %d, %Y"),
    }

    return render(request, "francis-artwork.html", context)


from django.shortcuts import render
from django.utils.timezone import now
from django.db.models.functions import TruncDate
from .models import Artwork

def Psalter(request):
    today_date = now().date()

    # Fetch today's Psalter Artwork and fix date filtering
    artwork = (
        Artwork.objects.annotate(upload_date=TruncDate("date_uploaded"))
        .filter(category="psalter_artwork", upload_date=today_date)
        .first()
    )

    print("DEBUG: Retrieved Artwork:", artwork)

    context = {
        "today_image_path_1": artwork.image1.url if artwork and artwork.image1 else None,
        "today_image_path_2": artwork.image2.url if artwork and artwork.image2 else None,
        "today_date": today_date.strftime("%B %d, %Y"),
    }

    return render(request, "psalter.html", context)


import os
from django.conf import settings
from django.shortcuts import render

def psalter_intro(request):
    """
    View to display the Psalter Introduction page with four images.
    """
    # Define the folder path
    psalter_intro_folder = os.path.join(settings.BASE_DIR, "static/gallery/psalterintro")

    # Image filenames (assuming they're named 1.jpg, 2.jpg, 3.jpg, 4.jpg)
    image_paths = []
    for i in range(1, 5):  # Loop through images 1 to 4
        img_path = f"gallery/psalterintro/{i}.jpg"  # Static relative path
        full_path = os.path.join(psalter_intro_folder, f"{i}.jpg")
        if os.path.exists(full_path):
            image_paths.append(img_path)

    context = {"image_paths": image_paths}

    return render(request, "psalter_intro.html", context)


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


from django.shortcuts import render
from .models import RetreatOffering

def RetreatCenter(request):
    offerings = RetreatOffering.objects.all()
    return render(request, 'retreat-center.html', {'offerings': offerings})



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


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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
                May you feel His presence and peace more profoundly each day.<br>
                For other information - retreats, visits, vocation, etc., please see our website: <a href="https://mepkinabbey.org" target="_blank">https://mepkinabbey.org</a>
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
    prayers = Prayer.objects.all()
    return render(request, 'list-of-prayers.html', {'prayers': prayers})

@login_required(login_url='pray')
def admin_list_of_prayers(request):
    prayers = Prayer.objects.all()
    return render(request, 'admin_dashboard/admin_list_of_prayers.html', {'prayers': prayers})

from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Prayer

@login_required(login_url='pray')
def admin_prayer_request(request):
    list_of_prayers = Prayer.objects.filter(type="Prayer Request").order_by("-created")
    paginator = Paginator(list_of_prayers, 10)  # Show 10 prayers per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin_dashboard/admin_prayer_request.html', {'page_obj': page_obj})

@login_required(login_url='pray')
def admin_gratitude_prayer(request):
    list_of_prayers = Prayer.objects.filter(type="Gratitude Prayer").order_by("-created")
    paginator = Paginator(list_of_prayers, 10)  # Show 10 prayers per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin_dashboard/admin_gratitude_prayer.html', {'page_obj': page_obj})


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


from django.utils.timezone import now as tz_now
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VisitorActivity  # Correct import for new model

@csrf_exempt
def update_activity(request):
    if request.method == 'POST':
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        ip_address = request.META.get('REMOTE_ADDR', '')

        # Ensure existing visitors are updated instead of being replaced
        visitor, created = VisitorActivity.objects.get_or_create(
            session_key=session_key,
            defaults={'first_visit': tz_now(), 'last_active': tz_now()}
        )

        # Update fields only if necessary (to avoid overwriting existing data)
        visitor.last_active = tz_now()
        if not visitor.ip_address:
            visitor.ip_address = ip_address
        visitor.total_time_spent += 60  # Assuming this function runs every minute
        visitor.save()

        return JsonResponse({"status": "success", "session_key": session_key})

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
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from datetime import datetime, timedelta
from pytz import timezone
from django.db.models import Count, Avg
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from collections import Counter  # Import Counter for counting URLs
from .models import VisitorActivity  # Ensure this import is here
from django.contrib.messages import get_messages

from django.utils.timezone import now
from datetime import datetime, timedelta
from django.db.models import Count, Avg
from collections import Counter
from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from .models import VisitorActivity  # Ensure the model is correctly imported

@login_required
def admin_dashboard(request):
    """ Fetches admin analytics, visitor tracking, and photo management data. """

    # Set the time zone to 'US/Eastern'
    eastern = timezone('US/Eastern')
    now_eastern = datetime.now(eastern)

    # 1️⃣ **Count future photos left for Francis Artwork**
    artwork_path = os.path.join(settings.BASE_DIR, 'static/gallery/Francis Artwork')
    photos = [f for f in os.listdir(artwork_path) if os.path.isfile(os.path.join(artwork_path, f)) and f.endswith(('.jpg', '.jpeg', '.png'))]

    future_photos = []
    for photo in photos:
        try:
            photo_date = datetime.strptime(photo.split('.')[0], "%B %d, %Y")
            photo_date = eastern.localize(photo_date)
            if photo_date > now_eastern:
                future_photos.append(photo)
        except ValueError:
            pass  # Ignore files that don’t match the date format

    # **Clear previous messages before adding new ones**
    storage = messages.get_messages(request)
    storage.used = True  # Mark messages as consumed

    if len(future_photos) <= 3:
        messages.warning(request, 'Only 3 or fewer future photos are left in the Francis Artwork section. Please upload more photos.')

    # 2️⃣ **Visitor Analytics**
    active_threshold = now() - timedelta(minutes=1)
    active_visitors_count = VisitorActivity.objects.filter(last_active__gte=active_threshold).count()

    total_visitors = VisitorActivity.objects.count()
    avg_session_duration = VisitorActivity.objects.aggregate(
        avg_duration=Avg('total_time_spent')
    )['avg_duration'] or 0

    # 3️⃣ **Extract Top Clicked URLs from `page_visits` JSONField**
    all_urls = VisitorActivity.objects.values_list('page_visits', flat=True)
    url_counter = Counter()

    for visits in all_urls:
        if isinstance(visits, dict):  # Ensure it's a dictionary
            url_counter.update(visits.keys())

    top_clicked_urls = url_counter.most_common(5)  # Get top 5 clicked URLs

    # **Prepare Data for Template**
    context = {
        'photos_left': len(future_photos),
        'total_visitors': total_visitors,
        'active_visitors_count': active_visitors_count,
        'avg_session_duration': round(avg_session_duration, 2),
        'top_clicked_urls': top_clicked_urls,
    }

    return render(request, 'admin_dashboard/admin_dashboard.html', context)




@login_required
def admin_edit(request):
    if request.method == 'POST':
        # Handle the form submission
        pass
    return render(request, 'admin_dashboard/edit.html')




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Artwork
import cloudinary.uploader
from datetime import datetime, timedelta
from django.utils.timezone import now

@login_required
def upload_artwork(request):
    if request.method == "POST" and request.FILES.getlist("photos"):
        section = request.POST.get("section")
        upload_type = request.POST.get("upload_type")
        start_date = request.POST.get("start_date")
        num_days = int(request.POST.get("num_days", 1))

        files = request.FILES.getlist("photos")[:2]  # Limit 2 images max

        # Validate input
        if not section or not start_date:
            messages.error(request, "Invalid input. Please try again.")
            return redirect("admin_dashboard")

        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()

        # Upload images for each day
        for i in range(num_days):
            upload_date = start_date_obj + timedelta(days=i)
            today_date_str = upload_date.strftime("%Y-%m-%d")

            # Upload to Cloudinary
            upload_results = []
            for j, file in enumerate(files):
                upload_result = cloudinary.uploader.upload(
                    file,
                    folder=f"{section}",
                    public_id=f"{today_date_str}_{j+1}",
                    overwrite=True,
                    resource_type="image"
                )
                upload_results.append(upload_result["secure_url"])

            # Save to database
            Artwork.objects.create(
                category=section,
                title=f"{section.replace('_', ' ').title()} - {today_date_str}",
                image1=upload_results[0] if len(upload_results) > 0 else None,
                image2=upload_results[1] if len(upload_results) > 1 else None,
                date_uploaded=upload_date
            )

        messages.success(request, "✅ Artwork uploaded successfully!")
        return redirect("admin_dashboard")

    return render(request, "admin_dashboard/upload_photo.html")


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from datetime import datetime
from pytz import timezone

@login_required
def upload_francis_artwork(request):
    if request.method == "POST" and request.FILES.getlist("photos"):
        files = request.FILES.getlist("photos")[:2]  # Max 2 images

        artwork = Artwork.objects.create(
            category="francis",
            title=f"Francis Artwork {now().strftime('%B %d, %Y')}",
            image1=files[0],
            image2=files[1] if len(files) > 1 else None
        )

        messages.success(request, "✅ Francis Artwork uploaded successfully!")
        return redirect("admin_dashboard")

    return render(request, "admin_dashboard/upload_photo.html")



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Artwork

@login_required
def upload_psalter_artwork(request):
    if request.method == "POST" and request.FILES.getlist("photos"):
        files = request.FILES.getlist("photos")[:2]  # Max 2 images

        artwork = Artwork.objects.create(
            category="psalter",
            title=f"Psalter Artwork {now().strftime('%B %d, %Y')}",
            image1=files[0],
            image2=files[1] if len(files) > 1 else None
        )

        messages.success(request, "✅ Psalter Artwork uploaded successfully!")
        return redirect("admin_dashboard")

    return render(request, "admin_dashboard/upload_photo.html")


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import RetreatOffering
from .forms import RetreatOfferingForm

@login_required
def manage_retreat_offerings(request):
    offerings = RetreatOffering.objects.all()
    return render(request, 'admin_dashboard/manage_retreat_offerings.html', {'offerings': offerings})

def add_retreat_offering(request):
    if request.method == 'POST':
        form = RetreatOfferingForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a retreat offering.')
            return redirect('admin_retreat_offerings')  # Redirect to the manage page
    else:
        form = RetreatOfferingForm()
    return render(request, 'admin_dashboard/add_retreat_offering.html', {'form': form})

@login_required
def edit_retreat_offering(request, pk):
    offering = RetreatOffering.objects.get(pk=pk)
    if request.method == 'POST':
        form = RetreatOfferingForm(request.POST, request.FILES, instance=offering)
        if form.is_valid():
            form.save()
            messages.success(request, 'Retreat Offering updated successfully.')
            return redirect('admin_retreat_offerings')
    else:
        form = RetreatOfferingForm(instance=offering)
    return render(request, 'admin_dashboard/edit_retreat_offering.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect

def DeleteRetreatOffering(request, pk):
    offering = get_object_or_404(RetreatOffering, pk=pk)
    if request.method == 'POST':
        offering.delete()
        messages.success(request, 'Retreat offering deleted successfully.')
        return redirect('admin_retreat_offerings')
    return redirect('admin_retreat_offerings')  # Redirect if method is not POST


# Src_App/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})




from django.utils.timezone import now
from django.http import JsonResponse
from django.shortcuts import render
from .models import VisitorActivity

def update_activity(request):
    """ Tracks visitor's time spent and most clicked URLs. """
    if request.method == 'POST':
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        visitor, created = VisitorActivity.objects.get_or_create(session_key=session_key)
        visitor.last_active = now()
        visitor.duration = (visitor.last_active - visitor.start_time).seconds  # Update duration
        visitor.save()

        return JsonResponse({"status": "success", "duration": visitor.duration})
    return JsonResponse({"status": "error"}, status=400)

def track_click(request):
    """ Stores most clicked URL per session. """
    if request.method == 'POST':
        session_key = request.session.session_key
        clicked_url = request.POST.get('url')

        if session_key and clicked_url:
            visitor = VisitorActivity.objects.filter(session_key=session_key).first()
            if visitor:
                visitor.most_clicked_url = clicked_url
                visitor.save()

        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)

def get_metrics(request):
    """ Returns site stats (e.g., average session duration, most clicked links). """
    total_visitors = VisitorActivity.objects.count()
    avg_session_duration = VisitorActivity.objects.aggregate(avg_duration=models.Avg('duration'))['avg_duration'] or 0
    top_clicked = VisitorActivity.objects.values('most_clicked_url').annotate(count=models.Count('most_clicked_url')).order_by('-count')[:5]

    return JsonResponse({
        "total_visitors": total_visitors,
        "avg_session_duration": avg_session_duration,
        "top_clicked_urls": list(top_clicked)
    })


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from collections import Counter
from datetime import timedelta
from django.utils.timezone import now
from django.http import JsonResponse
from .models import VisitorActivity

@login_required
def full_analytics_report(request):
    """Generates an in-depth report about the website's visitors and interactions."""

    total_visitors = VisitorActivity.objects.count()

    # Calculate average session duration
    avg_session_duration = VisitorActivity.objects.aggregate(avg_duration=Avg('total_time_spent'))['avg_duration'] or 0

    # Count live visitors in the last 5 minutes
    active_threshold = now() - timedelta(minutes=5)
    live_visitors = VisitorActivity.objects.filter(last_active__gte=active_threshold).count()

    # Extract the most clicked URLs
    all_urls = []
    for visitor in VisitorActivity.objects.all():
        if isinstance(visitor.page_visits, dict):
            all_urls.extend(visitor.page_visits.keys())

    url_counts = Counter(all_urls)
    top_clicked_urls = url_counts.most_common(10)  # Get top 10 most clicked URLs

    # Get visitor locations (assuming we store IP or location data)
    visitor_locations = VisitorActivity.objects.values('country').annotate(count=Count('country')).order_by('-count')

    return render(request, 'admin_dashboard/full_analytics_report.html', {
        'total_visitors': total_visitors,
        'avg_session_duration': round(avg_session_duration, 2),
        'live_visitors': live_visitors,
        'top_clicked_urls': top_clicked_urls,
        'visitor_locations': visitor_locations,
    })


import requests

def get_user_country(request):
    """Fetches the user's country using their IP address."""
    ip = request.META.get('REMOTE_ADDR', '')
    if ip == '127.0.0.1' or ip.startswith("192.168"):  # Handle local development
        return "Localhost"

    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return data.get("country", "Unknown")  # Get country code (e.g., US, CA)
    except Exception:
        return "Unknown"
