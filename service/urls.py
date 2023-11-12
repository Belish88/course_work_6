from django.urls import path

from service.apps import ServiceConfig
from service.views import MailingListView, MailingCreateView, LogListView, ClientListView, ClientCreateView, \
    MassageCreateView, MailingUpdateView, MailingDeleteView

app_name = ServiceConfig.name


urlpatterns = [
    path('mailing/', MailingListView.as_view(), name='mailing'),
    path('client/', ClientListView.as_view(), name='client'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('update_mailing/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
    path('create_massage/', MassageCreateView.as_view(), name='create_massage'),
    path('add_client/', ClientCreateView.as_view(), name='add_client'),
    path('log/', LogListView.as_view(), name='log'),
]
