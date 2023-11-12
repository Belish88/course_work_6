from django import forms

from service.models import Mailing, Client, Massage


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('name', 'periodic', 'start', 'status', 'is_active')


class MassageForm(forms.ModelForm):

    class Meta:
        model = Massage
        fields = ('title',)


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('email',)