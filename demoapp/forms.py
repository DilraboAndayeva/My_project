from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'birth_date', 'age', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting', 'style': 'color: green;'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangizni kiriting', 'style': 'color: green;'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998...', 'style': 'color: green;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email manzil', 'style': 'color: green;'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'color: green;'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Yoshingiz', 'style': 'color: green;'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Izoh...', 'style': 'color: green;'}),
        }