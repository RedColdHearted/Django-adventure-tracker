import datetime
import uuid

from django.db import models

from users.models import User


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.TextField()
    date = models.DateField(default=datetime.date.today, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}"


