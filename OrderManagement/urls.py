from django.urls import path
from .views import *

urlpatterns = [
    path('all/customers/', AllCustomers),
    path('customer/add/', customerAdd),
    path('customer/delete/<int:id>/', DeleteCustomer, name = 'delete_customer'),
    path('customer/update/<int:id>/', UpdateCustomer, name = 'update_customer'),
    
    path('order/add/', OrdersAdd),
    path('orders/', OrdersList),
    path('order/delete/<int:id>/', OrderDelete, name = 'delete_order'),
    path('order/update/<int:id>/', OrderUpdate, name = 'update_order'),
    
]