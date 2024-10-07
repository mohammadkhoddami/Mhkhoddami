from django.views import View
from core.models.index import IndexPageModel
from core.models.about import AboutMe
from core.models.experience import Exprience
from core.models.work import WorkModel
from core.models.blog import Blog
from django.shortcuts import render


class HomeView(View):
    def get(self, request):
        index_detail = IndexPageModel.objects.last()
        about_me = AboutMe.objects.last()
        exprience = Exprience.objects.all() 
        works = WorkModel.objects.all()
        blog = Blog.objects.all()
        
        context = {
            'index_detail' : index_detail,
            'about_me' : about_me,
            'experience' : exprience,
            'works' : works,
            'blog' : blog
        }
        return render(request, 'home/index.html',context)