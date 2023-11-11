from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from service.forms import MailingForm, ClientForm
from service.models import Mailing, Log, Client


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


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('service:client')
