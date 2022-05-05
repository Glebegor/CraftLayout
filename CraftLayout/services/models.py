from django.db import models
from PIL import Image

class OrderModel(models.Model):
    Title = models.CharField(max_length=255)
    BgImg = models.FileField(default='No_image.png', upload_to='orderimg')
    Text = models.TextField(max_length=2000)
    def __str__(self):
        return f'{self.Title} order'