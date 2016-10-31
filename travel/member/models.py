from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email', ]


# Create your models here.
