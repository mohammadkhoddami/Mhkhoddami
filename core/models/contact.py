from django.db import models
from core.models.base_model import BaseTimestampModel
from core.validators.phone_number import validate_phone_number

class ContactInfo(models.Model):
    title = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    linkedin = models.CharField(max_length=255)


class ContactNote(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12, validators=[validate_phone_number])
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return f'{self.name} with {self.email} and {self.phone_number} wrote a message'
