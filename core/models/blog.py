from django.db import models
from .base_model import BaseTimestampModel
from django.urls import reverse

class Blog(BaseTimestampModel,models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=155)
    body = models.TextField()
    meta_body = models.CharField(max_length=170, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('home:blog-detail', kwargs={'pk': self.pk})