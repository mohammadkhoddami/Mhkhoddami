from core.models.blog import Blog


class BlogModelMixin:
    """
    A mixin that provides Blog model for Views
    """
    model = Blog