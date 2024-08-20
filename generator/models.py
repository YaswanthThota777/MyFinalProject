from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'

class MusicFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    midi_file = models.CharField(max_length=255)
    wav_file = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
