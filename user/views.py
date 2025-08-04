import secrets

from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from user.forms import UserCreateForm


class UserRegisterView(CreateView):
    """Регистрация пользователя."""
    template_name = 'user/user_register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy("user:success_register")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()
        host = self.request.get_host()
        url = "http://{}/users/email-confirm/{}".format(host, user.token)
        send_mail(
            "Подтверждение почты в сервисе 'Кто же будет?'",
            "Перейдите по ссылке для завершения регистрации пользователя:\n{}".format(url),
            EMAIL_HOST_USER,
            [user.email],
        )
        return super().form_valid(form)


def success_register(request):
    if request.method == "GET":
        return render(request, "user/success_register.html")


