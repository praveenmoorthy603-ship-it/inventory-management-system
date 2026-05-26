from itertools import product

from urllib import request

from django.shortcuts import render, redirect

from .forms import *
from .models import *

from django.views import View


from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# # Product adding view
# def productAdd(request):
    
#     context={
#         'product_form': ProductForm()
#     }
    
#     if request.method == "POST":
#         product_new = ProductForm(request.POST)
#         if product_new.is_valid():
#             product_new.save()
    
#     return render(request, 'products_add.html', context)


# def AllProducts(request):
#     product_list = Product.objects.all()
    
#     return render(request, 'products.html', {'product_list': product_list})


# def DeleteProduct(request, id):
#     product = Product.objects.get(id=id)
#     product.delete()
#     return redirect('/inventory/products/')


# def UpdateProduct(request, id):
#     select_product = Product.objects.get(id=id)
#     context ={
#          'product_form': ProductForm(instance = select_product)
#     }
    
#     if request.method == "POST":
#         product_form = ProductForm(request.POST, instance=select_product)
#         if product_form.is_valid():
#             product_form.save()
            
#             return redirect('/inventory/products/')
   
#     return render(request, 'products_add.html', context)





class ProductsAddView(LoginRequiredMixin, View):
    
    login_url = '/'
    
    def get(self, request):
        context = {
            'product_form': ProductForm()
        }
    
        return render(request, 'products_add.html', context)


    def post(self, request):
        product_new = ProductForm(request.POST, request.FILES)
        if product_new.is_valid():
            product_new.save()
            return redirect('/inventory/products/')


class ProductListView(LoginRequiredMixin,View):
    
    login_url = '/'
    
    def get(self, request):
        product_list = Product.objects.all()
        return render(request, 'products.html', {'product_list': product_list})


class ProductDeleteView(LoginRequiredMixin, View):
    login_url = '/'
    
    def get(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('/inventory/products/')
    
class ProductUpdateView(LoginRequiredMixin, View):
    login_url = '/'
    
    def get(self, request, id):
        select_product = Product.objects.get(id=id)
        product_form = ProductForm(instance=select_product)
        return render(request, 'products_add.html', {'product_form': product_form})
    
    def post(self, request, id):
        select_product = Product.objects.get(id=id)
        product_form = ProductForm(request.POST, instance=select_product)
        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')