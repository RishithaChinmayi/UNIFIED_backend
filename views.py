from django.shortcuts import render, redirect
from .models import Bill, Payment
from .forms import PaymentForm
def bill_list(request):
 bills = Bill.objects.filter(user=request.user)
 return render(request, 'billpay/bill_list.html', {'bills': bills})
def create_payment(request, bill_id):
 bill = Bill.objects.get(id=bill_id)
 if request.method == 'POST':
 form = PaymentForm(request.POST)
 if form.is_valid():
 payment = form.save(commit=False)
 payment.bill = bill
 payment.save()
 return redirect('bill_list')
 else:
 form = PaymentForm()
 return render(request, 'billpay/create_payment.html', {'form': form, 'bill': bill})
