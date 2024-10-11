from core.models.work import WorkModel
from core.models.blog import Blog

def work_processor(request):
    works = WorkModel.objects.all()
    return {'works': works}

def blog_seo(request):
    meta_bodies = Blog.objects.values_list('meta_body', flat=True)
    return {'meta_blog': meta_bodies}