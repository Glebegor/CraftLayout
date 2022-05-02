from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Avatar = models.ImageField(default='default.png', upload_to='avatarks')
    banner = models.ImageField(default='default.png', upload_to='banners')
    position = models.CharField(default='Developer', max_length=150)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.Avatar.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.Avatar.path)

