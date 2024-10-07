from django.urls import path
from home.views.index import HomeView

urlpatterns = [
path('', HomeView.as_view(), name='home'),
    
]
