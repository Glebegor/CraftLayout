from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Exchange(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    salary = models.CharField(default='Agreements' ,max_length=255)
    text = models.TextField()
    technologies = models.CharField(max_length=255, default=' ')
    date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'Order {self.user} at {self.date}'