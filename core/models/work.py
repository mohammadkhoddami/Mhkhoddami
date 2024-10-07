from django.db import models

class WorkModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    image_2 = models.ImageField(null=True, blank=True)
    body = models.TextField()