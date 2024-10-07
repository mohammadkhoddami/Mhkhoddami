from django.views import generic
from core.models.blog import Blog
from core.mixins.useradmin import IsUserAdminMixin
from django.urls import reverse_lazy
from core.mixins.blogmodel import BlogModelMixin

class BlogListView(generic.ListView):
    queryset = Blog.objects.all()
    template_name = 'home/blog.html'
    context_object_name = 'blog'
    paginate_by = 7

class BlogCreateView(IsUserAdminMixin, BlogModelMixin, generic.CreateView):
    fields = '__all__'
    template_name = 'home/create-post.html'
    context_object_name = 'form'
    success_url = ('home:home')


class BlogDetailView(generic.DetailView, BlogModelMixin):
    context_object_name = 'post'
    template_name = 'home/detail-post.html'

class BlogUpdateView(IsUserAdminMixin, BlogModelMixin, generic.UpdateView):
    fields = '__all__'
    template_name = 'home/update-post.html'
    context_object_name = 'form'
    success_url = ('home:home')

class BlogDeleteView(IsUserAdminMixin, BlogModelMixin, generic.DeleteView):
    template_name = 'home/delete-post.html'
    success_url = reverse_lazy('home:home')