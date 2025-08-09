import secrets

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView

from config.settings import EMAIL_HOST_USER
from gender.models import Gender, GenderChoices
from user.forms import UserCreateForm, UserForm
from user.models import User


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
        url = "https://{}/users/email-confirm/{}/".format(host, user.token)
        send_mail(
            "Подтверждение почты в сервисе 'Кто же будет?'",
            "Перейдите по ссылке для завершения регистрации пользователя:\n{}".format(url),
            EMAIL_HOST_USER,
            [user.email],
        )
        self.request.session["success_register"] = True
        return super().form_valid(form)


class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Вывод информации о пользователе."""
    model = User

    def test_func(self):
        """Проверяем, что пользователь является владельцем объекта."""
        user = self.get_object()
        return self.request.user == user



class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Обновление информации о пользователе."""
    model = User
    form_class = UserForm

    def test_func(self):
        """Проверяем, что пользователь является владельцем объекта."""
        user = self.get_object()
        return self.request.user == user

    def get_success_url(self):
        return reverse_lazy("user:user_detail", kwargs={"pk": self.request.user.pk})


def success_register(request):
    """Страница успешной регистрации."""
    if request.method == "GET":
        if not request.session.get("success_register"):
            return redirect(reverse("gender:home_page"))
        del request.session["success_register"]
        return render(request, "user/success_register.html")


def email_verification(request, token):
    """
    Перевод пользователя в статуc Активный при проходе по ссылке с почты
    """
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = None
    user.save(update_fields=["is_active", "token"])
    Gender.objects.create(gender=GenderChoices.boy, user_id=user)
    Gender.objects.create(gender=GenderChoices.girl, user_id=user)
    return render(request, "user/email-confirm.html")
