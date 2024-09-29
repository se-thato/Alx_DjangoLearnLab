from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'recipient')
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
