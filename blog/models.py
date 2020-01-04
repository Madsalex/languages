from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # language = models.ForeignKey('Language', on_delete=models.CASCADE, default='other')
    language = models.CharField(max_length=40, default='other')
    # tags = models.TextField(default='none')
    tags = models.ManyToManyField('Tag')

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)
    favourite_tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
