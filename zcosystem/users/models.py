from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.template.loader import render_to_string
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

import stream_django
from stream_django import feed_manager
from stream_django.enrich import Enrich
from stream_django.activity import Activity

# User Profile
@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
    
    def __str__(self):
        return str(self.user.username)
    
    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name
    
    def get_url(self):
        return self.slug

# Country
@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(max_length=100, default="")
    short = models.CharField(max_length=100, default="")
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    
    def __str__(self):
        return str(self.name)

# City
@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(max_length=100, default="")
    slug = models.SlugField(unique=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
    
    def __str__(self):
        return str(self.name)

# User Event
@python_2_unicode_compatible
class UserEvent(Activity, models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'), related_name="%(class)s_posts")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    headline = models.CharField(max_length=30, blank=True)
    city = models.ForeignKey(City, blank=True, null=True)
    
    class Meta:
        verbose_name = 'User Event'
        verbose_name_plural = 'User Events'
    
    def __str__(self):
        return str(self.headline)
    
    @property
    def print_self(self):
        print(self.headline)
    
    @property
    def activity_object_attr(self):
        return self
    
    def save(self):
        super(UserEvent, self).save()
    
    @property
    def activity_notify(self):
        targets = []
        if self.city is not None:
            targets.append(feed_manager.get_feed('cityevents', self.city.slug.replace(" ", "_")))
        return targets














