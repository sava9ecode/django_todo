from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path("sign-up/", views.signup, name="signup"),
    path(
        "log-in/",
        auth_views.LoginView.as_view(template_name="userprofile/login.html"),
        name="login",
    ),
    path("log-out/", auth_views.LogoutView.as_view(), name="logout"),
]
