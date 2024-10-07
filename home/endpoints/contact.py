from django.urls import path
from home.views.contact import ContactMeView

urlpatterns = [
path('contact-me', ContactMeView.as_view(), name='contact-me'),
    
]
