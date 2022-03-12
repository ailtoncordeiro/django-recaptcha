from turtle import mode
from django.db import models

class Post(models.Model):
    
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name="Nome")
    text = models.TextField(blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True)
