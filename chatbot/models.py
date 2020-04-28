from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Message(models.Model):
    author = models.CharField(verbose_name="username", max_length=30, blank=True, null=True)
    #username        = models.CharField(verbose_name="username", max_length=30, blank=True)
    date_started     = models.DateTimeField(verbose_name='date started', auto_now_add=True)
    content = models.TextField()
    response = models.TextField()