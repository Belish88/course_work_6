from django import forms

from service.models import Mailing, Client, Massage


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('name', 'periodic', 'massage', 'start', 'stop', 'clients')


class MassageForm(forms.ModelForm):

    class Meta:
        model = Massage
        fields = ('title', 'text')


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('email', 'name', 'comment')
