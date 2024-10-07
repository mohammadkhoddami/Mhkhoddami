from django.views import View
from core.models.about import AboutMe
from django.shortcuts import render


class AboutMeView(View):
    def get(self, request):
        about_me = AboutMe.objects.last()
        return render(request, 'home/about.html', {'about_me': about_me})
