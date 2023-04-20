from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    image = models.ImageField(upload_to="media")

    def __str__(self):
        return self.name

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, verbose_name='username')
    

    