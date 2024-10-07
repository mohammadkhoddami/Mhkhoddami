from django.db import models


class AboutMe(models.Model):
    image = models.ImageField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mini_bio = models.TextField()
    cv_file = models.FileField(null=True, blank=True)