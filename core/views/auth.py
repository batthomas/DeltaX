from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View

from ..forms import LoginForm


class AnonymousRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("tasks_overview")
        return super(AnonymousRequiredMixin, self).dispatch(request, *args, **kwargs)


class AuthenticationRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        self.login_url = "auth_login"
        self.redirect_field_name = "redirect_to"
        return super(AuthenticationRequiredMixin, self).dispatch(request, *args, **kwargs)


class LoginView(AnonymousRequiredMixin, View):
    template_name = "auth/login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect("tasks_overview")
        return render(request, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect("auth_login")
