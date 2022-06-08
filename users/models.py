from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinLengthValidator

class CustomUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    post_code = models.CharField(validators=[MinLengthValidator(10)], max_length=10)
    contact_phone_number = models.CharField(validators=[MinLengthValidator(10)], max_length=10)

    def __str__(self):
        return f"CustomUser: {self.username}"