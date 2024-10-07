from django.db import models
from django_jalali.db import models as jmodels


class Exprience(models.Model):
    subtitle = models.CharField(max_length=40)
    body = models.TextField()
    since = jmodels.jDateField(null=True, blank=True)
    till = jmodels.jDateField(null=True, blank=True)
    current = models.BooleanField()

class MySkill(models.Model):
    title = models.CharField(max_length=50)
    number_percentage = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.title} - {self.number_percentage}'