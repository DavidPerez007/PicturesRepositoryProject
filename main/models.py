from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    image = models.BinaryField()