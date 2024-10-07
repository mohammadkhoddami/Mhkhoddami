from django.views import generic, View
from core.models.experience import Exprience, MySkill
from core.models.index import IndexPageModel
from django.shortcuts import render


class ExprienceList(View):
    def get(self, request):
        picture = IndexPageModel.objects.last().exprience_image.url
        experience = Exprience.objects.all()
        skills = MySkill.objects.all()
        return render(request, 'home/experiences.html', {'skills': skills,
                                                         'experiences': experience,
                                                         'picture': picture})