from django.urls import path
from home.views.about import AboutMeView

urlpatterns = [
path('about-me',AboutMeView.as_view(), name='about-me')
    
]
