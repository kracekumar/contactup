from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100,
                                 min_length=3)
    last_name = forms.CharField(max_length=100,
                                required=False)
    phone_no = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(required=False)


class DeleteForm(forms.Form):
    pass
