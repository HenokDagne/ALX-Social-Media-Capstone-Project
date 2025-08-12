from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class CustomUser(AbstractUser):
    phone_regex = RegexValidator(
         regex=r'^\+?[1-9]\d{1,14}$',  # E.164 international format
        message="Phone number must be entered in the format: '+<countrycode><number>' (up to 15 digits)."
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=16,
        unique=True,
        blank=True,
        null=True,
    )
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

