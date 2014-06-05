import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget

years = range(1950, datetime.datetime.now().year)


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100,
                                 min_length=3)
    last_name = forms.CharField(max_length=100,
                                required=False)
    phone_no = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(required=False)
    website = forms.URLField(required=False)
    relationship = forms.CharField(required=False)
    notes = forms.CharField(widget=forms.TextInput())
    birthday = forms.DateField(widget=SelectDateWidget(required=False,
                                                       years=years),
                               required=False)
class DeleteForm(forms.Form):
    pass
