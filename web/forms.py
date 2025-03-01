from django import forms
from django.forms import widgets
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control", "placeholder":"Name"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder":"Email ",}),
            "phone": widgets.TextInput(attrs={"class": "required form-control","placeholder":"Phone Number",}),
            "message": widgets.Textarea(attrs={"class": "required form-control","placeholder":"Message",}),
        }