from django import forms
from .models import Payment
class PaymentForm(forms.ModelForm):
 amount_paid = forms.DecimalField(max_digits=8, decimal_places=2)
 class Meta:
 model = Payment
 fields = ('payment_date',)
 def clean(self):
 cleaned_data = super().
