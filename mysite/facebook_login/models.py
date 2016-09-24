# from django.db import models

# class facebook_user(models.Model):
# 	name_text = models.CharField(max_length=50)
# 	profile_pic = models.ImageField()
# 	access_token = models.CharField(max_length=200)
# 	is_active = models.BooleanField(default=False)
# 	def __str__(self):
# 		return self.name_text

# Define a custom User class to work with django-social-auth
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
