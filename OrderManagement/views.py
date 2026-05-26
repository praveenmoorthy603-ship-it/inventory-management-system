from django.shortcuts import render, redirect

from .forms import *
from .models import *

#for login required fuction base views
from django.contrib.auth.decorators import login_required

# Create your views here.

# Customer adding view

@login_required(login_url='/')
def customerAdd(request):
    
    context={
        'customer_form': CustomerForm()
    }
    
    if request.method == "POST":
        customer_new = CustomerForm(request.POST)
        if customer_new.is_valid():
            customer_new.save()
            return redirect('/orders/all/customers/')

        else:

            print(customer_new.errors)

    return render(request, 'customers_add.html', context)    

    
@login_required(login_url='/')      
def AllCustomers(request):
    customer_list = Customer.objects.all()
    print(customer_list)
    return render(request, 'customers.html', {'customer_list': customer_list})


@login_required(login_url='/')
def DeleteCustomer(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('/orders/all/customers/')


@login_required(login_url='/')
def UpdateCustomer(request, id):
    select_customer = Customer.objects.get(id=id)
    context ={
         'customer_form': CustomerForm(instance=select_customer)
    }
     
    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=select_customer)
        if customer_form.is_valid():
            customer_form.save()
            
            return redirect('/orders/all/customers/')
   
    return render(request, 'customers_add.html', context)




@login_required(login_url='/')
def OrdersAdd(request):
    context ={
        'order_form': OrdersForm() 
    }
    
    if request.method == 'POST':
        selected_product = Product.objects.get(id = request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        
        gst_amount = (amount * selected_product.gst) / 100
        
        total_amount = amount + gst_amount  
        
        new_order = Orders(customer_reference_id = request.POST['customer_reference'],
                    product_reference_id = request.POST['product_reference'],
                    order_number = request.POST['order_number'],
                    order_date = request.POST['order_date'],
                    quantity = request.POST['quantity'],
                    amount = amount,
                    gst_amount = gst_amount,
                    total_amount = total_amount)
        new_order.save()
        return redirect('/orders/orders/')

    return render(request, 'orders_add.html', context)



@login_required(login_url='/')
def OrdersList(request):
    order_list = Orders.objects.all()
    return render(request, 'orders.html', {'order_list': order_list})


@login_required(login_url='/')
def OrderDelete(request,id):
    delete = Orders.objects.get(id = id)
    delete.delete()
    return redirect('/orders/orders/')


@login_required(login_url='/')
def OrderUpdate(request, id):
    update = Orders.objects.get(id = id)
    context = {
        'order_form': OrdersForm(instance=update)
    }
    
    if request.method == 'POST':
        selected_product = Product.objects.get(id = request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        
        gst_amount = (amount * selected_product.gst) / 100
        
        total_amount = amount + gst_amount  
        
        order_filter = Orders.objects.filter(id = id)
        
        order_filter.update(
            customer_reference_id = request.POST['customer_reference'],
            product_reference_id = request.POST['product_reference'],
            order_number = request.POST['order_number'],
            order_date = request.POST['order_date'],
            quantity = request.POST['quantity'],
            amount = amount,
            gst_amount = gst_amount,
            total_amount = total_amount
        )

        return redirect('/orders/orders/')
    
    return render(request, 'orders_add.html', context)