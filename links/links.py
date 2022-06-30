import django
from django.db import models
from django.contrib.auth.models import ForeignKey
from django.contrib.auth.models import User

class Post(models.Model):
 target_url=models.URLFiels(max_length=200)
 description=models.CharField(max_length=200)
 identifier=models.SlugField(max_length=20, blank=True, unique=True)
 author=models.ForeignKey(get_user_model())
 created_date =models.DateTimeField
 active=models.BooleanField(default=True)

def __str__(self):
 return self.target_url

