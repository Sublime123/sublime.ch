from email.policy import default
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    msg = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pics')