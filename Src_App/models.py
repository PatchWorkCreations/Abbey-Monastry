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
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
