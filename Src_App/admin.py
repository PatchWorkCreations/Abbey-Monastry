from django.contrib import admin
from .models import *


class ImageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Check if any object exists in the database
        existing_objects_count = Image.objects.count()

        # Allow adding a new object only if no object exists
        if existing_objects_count == 0:
            return True
        else:
            return False


class TextAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Check if any object exists in the database
        existing_objects_count = Text.objects.count()

        # Allow adding a new object only if no object exists
        if existing_objects_count == 0:
            return True
        else:
            return False


admin.site.register(ArtWork)
admin.site.register(Image, ImageAdmin)
admin.site.register(Text, TextAdmin)
admin.site.site_header = "MEPKIN ABBEY ADMIN"
