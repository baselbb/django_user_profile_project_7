"""Importing Models module, django built-in User module
and Signals modules create, save and update Profile model
with User model once created
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from tinymce.models import HTMLField


# Profile model extending django's built in:
# User model(first_name, last_name, password, email)
# OneToOneField so >>> user=User.objects.get(pk=1) >>> hasattr(user, 'Profile') >>> True
class Profile(models.Model):
    """Using OneToOneField to link extended Profile
    model fields to django User model"""

    # Using related_named we can get >>> profile = request.user.profile
    # Avatar profile pic saved to MEDIA folder in accounts/media
    # See settings.py for MEDIA folder settings

    user = models.OneToOneField(User,
                                related_name='profile',
                                on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    bio = HTMLField(blank=True)
    avatar = models.ImageField(upload_to='avatars/',
                               blank=True)

    city = models.CharField(max_length=50, blank=True)
    country = CountryField(blank=True)
    hobby = models.CharField(max_length=100, blank=True)


# Signals methods to create and save user profile extended model once a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()