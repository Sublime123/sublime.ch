from email.policy import default
from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
def only_filename(instance, filename):
    return filename

class Post(models.Model):    
    number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256,default="",blank=True)
    msg = models.CharField(max_length=1000,default="",blank=True)
    img = models.ImageField(upload_to=only_filename,null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    published_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.msg
