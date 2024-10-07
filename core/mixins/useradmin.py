from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponseRedirect


class IsUserAdminMixin(UserPassesTestMixin):
    """
    Mixin to check if the requested user is superuser or not
    """
    
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self) -> HttpResponseRedirect:
        raise PermissionDenied("Sorry! :) ")