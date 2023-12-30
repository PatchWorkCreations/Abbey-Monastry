from django.db import models


class Image(models.Model):
    index = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                              verbose_name='Index Image')

    header = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                               verbose_name='Header Image')

    the_gardens = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                    verbose_name='The Gardens Image')
    the_brothers = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                     verbose_name='The Brothers Image')
    retreat_center = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                       verbose_name='Retreat Center Image')

    virtual_tour = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                     verbose_name='Virtual Tour Image')
    the_gardens_and_scenery = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                                verbose_name='The Gardens & Scenery Image')
    meditation_garden = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                          verbose_name='Meditation Garden of Truth & Reconciliation Image')

    who_we_are = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                   verbose_name='Who We Are Image')
    our_daily_life = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                       verbose_name='Our Daily Life Image')
    vacation = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                 verbose_name='Vacation Image')
    pray_with_us = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                     verbose_name='Pray With Us Image')

    watch_video = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                    verbose_name='Watch Video Image')
    about_the_center = models.ImageField(upload_to='dynamic_images', null=True, blank=True,
                                         verbose_name='About the Center Image')

    def __str__(self):
        return "Modify Images"


class Text(models.Model):
    our_lady_of_mepkin = models.TextField(verbose_name="Our Lady of Mepkin Text", null=True, blank=True)
    lauren_cemetry = models.TextField(verbose_name="Lauren's Cemetry Text", null=True, blank=True)

    def __str__(self):
        return "Modify Texts"


class ArtWork(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='artworks', default='', blank=False)

    def __str__(self):
        return self.title
