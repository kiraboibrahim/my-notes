from django.contrib.auth import views as auth_views

from .forms import SigninForm


class LoginView(auth_views.LoginView):
    template_name = 'accounts/signin.html'
    form_class = SigninForm
