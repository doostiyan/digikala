from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=12, unique=True)
    address1 = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=120)

    def __str__(self):
        return self.user.username

def create_profile(sender, created, instance, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)