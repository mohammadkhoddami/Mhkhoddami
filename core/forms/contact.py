from django import forms
from core.models.contact import ContactNote

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactNote
        fields = ('name', 'phone_number', 'email', 'message')