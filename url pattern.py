from django.urls import path
from . import views
urlpatterns = [
 path('bills/', views.bill_list, name='bill_list'),
 path('bills/<int:bill_id>/pay/', views.create_payment, name='create_payment'),
]
