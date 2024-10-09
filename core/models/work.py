from django.db import models
from django.urls import reverse
class WorkModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    image_2 = models.ImageField(null=True, blank=True)
    body = models.TextField()
    link = models.CharField(max_length=545, default='https://www.mhkhoddami.ir')
    
    
    def get_absolute_url(self):
        return reverse("home:works-detail", kwargs={"pk": self.pk})
    