from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView

from users.forms import UserRegisterForm
from users.models import User


@login_required
def main(request):
    return render(request, 'users/main.html')


class UserListView(ListView):
    model = User


@login_required
def users_active(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect(reverse('users:users_list'))




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


@login_required
def activate(request, token):
    user = User.objects.get(token=token)
    user.email_verify = True
    user.save()
    return render(request, 'users/activate.html')

