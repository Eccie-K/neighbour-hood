from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from smartfields import fields
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Hood(models.Model):
    name = models.CharField(max_length=40, null=True)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(null=True)
    link = models.URLField()
    user = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    location = models.CharField(max_length = 40, null = True)
    occupants = models.IntegerField(null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def save_hood(self):
        return  self.save()

    def delete_hood(self):
        return self.delete()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    dob = models.DateTimeField(blank=True, null = True)
    bio = models.CharField(max_length = 250, null=True)
    avatar = fields.ImageField(upload_to = 'uploads/')
    hood = models.CharField(max_length = 30, blank=True, null=True)
    hobby = models.CharField(max_length = 200, blank=True, null=True)


    def create_user_profile(sender, instance, created, **kwargs):

        if created:
            profile.objects.create(user=instance)


            post_save.connect(create_user_profile, sender=User)

