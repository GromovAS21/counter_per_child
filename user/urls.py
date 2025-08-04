from django.urls import path

from user.apps import UserConfig
from user.views import UserRegisterView, success_register

app_name = UserConfig.name

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user_register"),
    path("success-register/", success_register, name="success_register"),
    path("login/", success_register, name="login"),
]