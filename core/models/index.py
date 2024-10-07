from django.db import models


class IndexPageModel(models.Model):
    #About Me in Landing
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    exprience_image = models.ImageField()
    github = models.CharField(max_length=40)
    linkedin = models.CharField(max_length=40)
    telegram = models.CharField(max_length=40)
    