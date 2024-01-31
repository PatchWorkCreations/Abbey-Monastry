from django.db import models


class Prayer(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    prayer_msg = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MepkinDailyWord(models.Model):
    post = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post
