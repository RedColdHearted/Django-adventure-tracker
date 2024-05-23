import uuid
import os

from django.contrib.auth.models import AbstractUser
from django.db import models

def get_profile_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('profile_images', new_filename)


class User(AbstractUser):
    profile_image = models.ImageField(upload_to=get_profile_image_upload_path, blank=True, null=True)

    def __str__(self):
        return self.username