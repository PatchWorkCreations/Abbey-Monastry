from django.db import models


class PrayerRequest(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    prayer_request = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
