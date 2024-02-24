from django.db import models
from django.contrib.auth.models import User
class Bill(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=255)
 amount = models.DecimalField(max_digits=8, decimal_places=2)
 due_date = models.DateField()
class Payment(models.Model):
 bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
 payment_date = models.DateField()
 amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
