from django.views import generic
from django.urls import reverse_lazy
from core.models.work import WorkModel
from core.mixins.useradmin import IsUserAdminMixin
from core.mixins.workmodel import WorkModelMixin

class WorkList(generic.ListView):
    queryset = WorkModel.objects.all()
    template_name = 'home/work.html'
    context_object_name = 'works'
    paginate_by = 7

class WorkCreate(IsUserAdminMixin, WorkModelMixin, generic.CreateView):
    fields = '__all__'
    template_name = 'home/work-create.html'
    context_object_name = 'form'

class WorkDetail(generic.DetailView, WorkModelMixin):
    context_object_name = 'work'
    template_name = 'home/work-single.html'

class WorkUpdate(IsUserAdminMixin, WorkModelMixin, generic.UpdateView):
    fields = '__all__'
    template_name = 'home/work-update.html'
    context_object_name = 'form'
    success_url = ('home:home')

class WorkDelete(IsUserAdminMixin, WorkModelMixin, generic.DeleteView):
    template_name = 'home/work-delete.html'
    success_url = reverse_lazy('home:home') #TODO Change this to work Detail also for other views too     

