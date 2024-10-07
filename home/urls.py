from itertools import chain
from .endpoints.about import urlpatterns as about_urlpatterns
from .endpoints.blog import urlpatterns as blog_urlpatterns
from .endpoints.contact import urlpatterns as contact_urlpatterns
from .endpoints.index import urlpatterns as index_urlpatterns
from .endpoints.experience import urlpatterns as service_urlpatterns
from .endpoints.work import urlpatterns as work_urlpatterns


app_name = 'home'

urlpatterns = list(chain(
    about_urlpatterns,
    blog_urlpatterns,
    contact_urlpatterns,
    index_urlpatterns,
    service_urlpatterns,
    work_urlpatterns
))