from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, related_name='+')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # language = models.ForeignKey('Language', on_delete=models.CASCADE, default='other')
    language = models.CharField(max_length=40, default='other')
    # tags = models.TextField(default='none')
    tags = models.ManyToManyField('Tag', blank=True)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    languages = models.ManyToManyField(Language, blank=True, related_name='+')
    native = models.ForeignKey(Language, blank=True, on_delete=models.SET_NULL, null=True, related_name='+')
    favourite_tags = models.ManyToManyField(Tag, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
