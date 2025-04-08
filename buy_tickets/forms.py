from django import forms
from .models import PaymentCard

class PaymentCardForm(forms.ModelForm):
    class Meta:
        model = PaymentCard
        fields = ['number', 'expiration_date', 'card_name', 'company_card']
        # datepicker for the expiration date
        widgets = {
            'expiration_date': forms.DateInput(
                attrs={
                    'type': 'date',  
                    'class': 'form-control'
                }
            ),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'card_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_card': forms.TextInput(attrs={'class': 'form-control'}),
        }
