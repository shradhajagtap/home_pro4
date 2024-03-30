from django import forms
from .models import HotelBooking


class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = "__all__"

        widgets = {
            "customer_first_first": forms.TextInput(attrs={"class": "form-control"}),
            "customer_last_last": forms.TextInput(attrs={"class": "form-control"}),
            "customer_address": forms.Textarea(attrs={"class": "form-control"}),
            "customer_email": forms.EmailInput(),
            "customer_phone_no": forms.NumberInput()
        }
