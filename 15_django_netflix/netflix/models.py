from django.db import models
from django.contrib.auth.models import User

import uuid
# Create your models here.


class Profile(models.Model):

    AGE_CHOICES = (
        ('All', 'All'),
        ('Kids', 'Kids')
    )

    user = models.ForeignKey(User, blank=True, related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
    )
    AGE_CHOICES = (
        ('All', 'All'),
        ('Kids', 'Kids'),
    )
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)  # uuid.uuid4 ifadesi ise, Python'ın uuid modülündeki uuid4() fonksiyonunu çağırarak rasgele bir UUID (Universally Unique Identifier) oluşturur.
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ForeignKey('Video', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title