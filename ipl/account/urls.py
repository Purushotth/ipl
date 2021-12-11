from django.urls import include, path, re_path

from .views import *

urlpatterns = [
    re_path('login/?$', LoginView.as_view(), name='login'),
    re_path('logout/?$', LogoutView.as_view(), name='logout'),
]