from django.urls import path

from service.apps import ServiceConfig
from service.views import MailingListView, MailingCreateView, LogListView, ClientListView, ClientCreateView

app_name = ServiceConfig.name


urlpatterns = [
    path('mailing', MailingListView.as_view(), name='mailing'),
    path('client', ClientListView.as_view(), name='client'),
    path('create_mailing', MailingCreateView.as_view(), name='create_mailing'),
    path('add_client', ClientCreateView.as_view(), name='add_client'),
    path('log', LogListView.as_view(), name='log'),
]
