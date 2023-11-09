from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:email_verify')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Подтвердите почту',
            message=f'Пройдите по ссылке http://127.0.0.1:8000/activate/{new_user.token}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def activate(request, token):
    user = User.objects.get(token=token)
    user.email_verify = True
    user.save()
    return render(request, 'users/activate.html')

