from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views as accounts_views

urlpatterns = [
    path("signin", accounts_views.LoginView.as_view(), name="signin"),
    path("signout", LogoutView.as_view(), name="signout")
]
