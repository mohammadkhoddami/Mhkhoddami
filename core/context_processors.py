from core.models.work import WorkModel


def work_processor(request):
    works = WorkModel.objects.all()
    return {'works': works}