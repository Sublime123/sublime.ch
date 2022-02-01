from email.policy import default
from types import NoneType
from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Post(models.Model):    
    number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256,null=True, blank=True)
    msg = models.CharField(max_length=1000,null=True, blank=True)
    img = models.ImageField(upload_to='pics',null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    published_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.msg
