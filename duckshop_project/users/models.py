from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField

# Create your models here.

class CustomUser(AbstractUser):
    phone = PhoneField(blank=True, help_text='Contact phone number')