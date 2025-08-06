from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.apps import UserConfig
from user.views import UserRegisterView, success_register, email_verification

app_name = UserConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="user/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserRegisterView.as_view(), name="user_register"),
    path("success-register/", success_register, name="success_register"),
    path("email-confirm/<str:token>/", email_verification, name="email_verification"),
]
