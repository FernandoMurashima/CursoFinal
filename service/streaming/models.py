from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    """
    User model

    Please note that fields first_name, last_name and email are defined in the superclass (AbstractUser).
    """

    class Type(models.TextChoices):
        REGULAR = 'Regular', _('Regular')
        ADMIN = 'Admin', _('Admin')

    type = models.CharField(max_length=50, choices=Type.choices, default=Type.REGULAR)
    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=500, blank=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Movie(models.Model):
    """
    Movie model
    """
    title = models.CharField(max_length=50, blank=True)
    year = models.IntegerField()
    cover = models.URLField(blank=True)
    description = models.TextField(blank=True)
    midia = models.URLField(blank=True)


class Favourite(models.Model):
    """
    Favourite relation model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class MovieWatched(models.Model):
    """
    Movie watched relation model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
