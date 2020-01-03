from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Language(models.Model):
    # id = models.PositiveIntegerField()
    pass


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # language = models.ForeignKey('Language', on_delete=models.CASCADE, default='other')
    language = models.CharField(max_length=40, default='other')
    # tags = models.TextField(default='none')
    tags = models.TextField(default='none')

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

