from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True, null=True, default='default_avatar.png')
    facebook_profile = models.URLField(blank=True, null=True)

