from django.db import models


class Prayer(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    prayer_msg = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MepkinDailyWord(models.Model):
    post = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post

    class Meta:
        ordering = ['-created']


class Bio(models.Model):
    content = models.CharField(max_length=200, default='Add Bio')

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        # Check if there is an existing instance
        existing_instance = Bio.objects.first()

        # If an instance exists, update the content instead of creating a new instance
        if existing_instance:
            existing_instance.content = self.content
            existing_instance.save()
        else:
            super().save(*args, **kwargs)


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    session_key = models.CharField(max_length=40)  # Django's default session key length
    timestamp = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    current_page = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.ip_address} - Session {self.session_key} on {self.current_page} at {self.last_active}"



from django.db import models
import datetime

class RetreatOffering(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)  # New end_date field
    location = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='retreatofferings/', null=True, blank=True)
    registration_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "No Title"


from django.db import models
from django.utils import timezone


class VisitorActivity(models.Model):
    session_key = models.CharField(max_length=255, unique=True)
    first_visit = models.DateTimeField(default=timezone.now)  # Provide default value
    last_active = models.DateTimeField(auto_now=True)
    total_time_spent = models.IntegerField(default=0)
    page_visits = models.JSONField(default=dict)
    country = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"Session: {self.session_key} | Visits: {self.page_visits}"

from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.utils.timezone import now

class Artwork(models.Model):
    CATEGORY_CHOICES = [
        ("psalter", "Psalter Artwork"),
        ("francis", "Francis Artwork"),
    ]

    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="psalter"
    )
    title = models.CharField(max_length=200, help_text="Title of the artwork")
    image1 = CloudinaryField("image", help_text="First artwork image")
    image2 = CloudinaryField("image", blank=True, null=True, help_text="Second artwork image")
    date_uploaded = models.DateTimeField(default=now, help_text="Timestamp of artwork upload")

    def __str__(self):
        return f"{self.get_category_display()} - {self.title} ({self.date_uploaded.date()})"
    
    class Meta:
        ordering = ["-date_uploaded"]  # Show newest first
