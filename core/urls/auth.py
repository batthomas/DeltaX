from django.urls import path

from ..views.auth import *

urlpatterns = [
    path("login/", LoginView.as_view(), name="auth_login"),
    path("logout/", LogoutView.as_view(), name="auth_logout")
]
