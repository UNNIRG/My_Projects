from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    avatar = models.ImageField(
        upload_to='avatars/', null=True, blank=True, default='avatars/Obiwan.png')

    def __str__(self):
        return self.title
