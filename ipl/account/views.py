from django.shortcuts import render

from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import *


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = AccountLoginForm()
        self.context = {
            'form': form,
        }
        return render(request, "Login.html", self.context)

    def post(self, request, *args, **kwargs):
        post_params = self.request.POST.copy()
        email = post_params.get('email')
        user = authenticate(username=email.lower(), password=post_params.get('password'))
        if user is not None:
            login(request, user)
            request.session.update({
                'account_login': True
            })
            return HttpResponseRedirect(reverse('application:landingpage'))
        else:
            form = AccountLoginForm(initial={
                'email': email
            })
            self.context = {
                'error': 1,
                'error_msg': "Invalid Credentials",
                'form': form
            }
            return render(request, "Login.html", self.context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            logout(self.request)
            request.session.update({
                'account_login': False
            })
        form = AccountLoginForm()
        self.context = {
            'form': form,
            'logout': 1
        }
        return render(request, "Login.html", self.context)

    def post(self, request, *args, **kwargs):
        return LoginView.as_view()(request, *args, **kwargs)