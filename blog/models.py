from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption1 = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='images/', blank=True)
    caption2 = models.TextField(blank=True)
    image2 = models.ImageField(upload_to='images/', blank=True)
    caption3 = models.TextField(blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    caption4 = models.TextField(blank=True)
    image4 = models.ImageField(upload_to='images/', blank=True)
    caption5 = models.TextField(blank=True)
    image5 = models.ImageField(upload_to='images/', blank=True)
    caption6 = models.TextField(blank=True)
    image6 = models.ImageField(upload_to='images/', blank=True)
    caption7 = models.TextField(blank=True)
    image7 = models.ImageField(upload_to='images/', blank=True)
    caption8 = models.TextField(blank=True)
    image8 = models.ImageField(upload_to='images/', blank=True)
    caption9 = models.TextField(blank=True)
    image9 = models.ImageField(upload_to='images/', blank=True)
    caption10 = models.TextField(blank=True)
    image10 = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

