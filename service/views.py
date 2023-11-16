import os
import smtplib
from datetime import timedelta, datetime

from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand
from django.core.serializers import python
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from service.const import CREATED, NO_ACTIVE, START
from service.forms import MailingForm, ClientForm, MassageForm
from service.jobs import job_rady_check
from service.management.commands.mailing import Command
from service.models import Mailing, Log, Client, Massage


class MailingListView(ListView):
    model = Mailing
    ordering = ['is_active', '-status', 'start']

    def get_queryset(self):
        queryset = super().get_queryset()
        job_rady_check()
        return queryset


class MailingDetailView(DetailView):
    model = Mailing

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset


class ClientDetailView(DetailView):
    model = Client

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset



class LogListView(ListView):
    model = Log
    ordering = ['-time_attempt']


class ClientListView(ListView):
    model = Client


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('service:mailing')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('name', 'periodic', 'massage', 'start', 'stop', 'clients')
    success_url = reverse_lazy('service:mailing')


class ClientUpdateView(UpdateView):
    model = Mailing
    fields = ('email', 'name', 'comment')
    success_url = reverse_lazy('service:client')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('service:mailing')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('service:client')



class MassageCreateView(CreateView):
    model = Massage
    form_class = MassageForm
    success_url = reverse_lazy('service:create_mailing')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('service:client')


def activate_mailing(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if mailing.is_active:
        mailing.is_active = False
        mailing.status = NO_ACTIVE
    else:
        mailing.is_active = True
        mailing.status = CREATED
    mailing.save()
    return redirect(reverse('service:mailing'))


def automatic_mailing(request):
    # os.system('cd service/management/commands/mailing.py')
    return redirect(reverse('service:mailing'))


def start_mailing(request, pk):
    log = Log()
    mail = Mailing.objects.get(pk=pk)
    mail.start = START + timedelta(minutes=mail.periodic)
    mailing_clients = mail.clients.all()
    for client in mailing_clients:
        try:
            send_mail(
                subject=mail.massage.title,
                message=mail.massage.text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email]
            )
        except smtplib.SMTPAuthenticationError:
            print('Ошибка smtplib.SMTPAuthenticationError:')
            log.mail_server_response = 'Ошибка smtplib.SMTPAuthenticationError:'

        log.name = mail.name
        log.time_attempt = datetime.now()
        if log.mail_server_response:
            log.status = 'Не отправлено'
        else:
            log.status = 'Отправлено'
            log.mail_server_response = ''
        log.mode = 'Ручной'
    mail.save()
    log.save()
    return redirect(reverse('service:mailing'))