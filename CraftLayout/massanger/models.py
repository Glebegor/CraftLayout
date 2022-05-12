from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MassangerModel(models.Model):
    username = models.ForeignKey(User, verbose_name="Username", on_delete=models.CASCADE)
    Text = models.TextField(default=' ')
    SendTo = models.CharField(default='', max_length=255)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'send from {self.username} to {self.SendTo}'
