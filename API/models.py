from django.db import models
from django.contrib.auth.models import User


class API(models.Model):
    title = models.CharField( max_length=50)
    bodey = models.CharField( max_length=50)
    created_at =models.DateTimeField(auto_now_add=True)
    created_at =models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
