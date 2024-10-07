from django.urls import path
from home.views.blog import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
path('blog/', BlogListView.as_view(), name='blog'),
path('blog/craete/', BlogCreateView.as_view(), name='blog-create'),
path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'), 
]
