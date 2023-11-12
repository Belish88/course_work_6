from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from service.forms import MailingForm, ClientForm, MassageForm
from service.models import Mailing, Log, Client, Massage


class MailingListView(ListView):
    model = Mailing


class LogListView(ListView):
    model = Log


class ClientListView(ListView):
    model = Client


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('service:mailing')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('service:mailing')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('service:mailing')


class MassageCreateView(CreateView):
    model = Massage
    form_class = MassageForm
    success_url = reverse_lazy('service:create_mailing')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('service:client')
