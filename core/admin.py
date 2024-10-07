from django.contrib import admin
from core.models.about import AboutMe
from core.models.blog import Blog
from core.models.contact import ContactNote, ContactInfo
from core.models.index import IndexPageModel
from core.models.experience import Exprience, MySkill
from core.models.work import WorkModel
# Register your models here.


required_models = [
    AboutMe,
    Blog,
    ContactInfo,
    ContactNote,
    IndexPageModel,
    Exprience,
    WorkModel,
    MySkill
]
admin.site.register(required_models)