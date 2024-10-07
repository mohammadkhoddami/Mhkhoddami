from django.urls import path
from home.views.experience import ExprienceList

urlpatterns = [
path('experience/', ExprienceList.as_view(), name='experience-list'),
]
