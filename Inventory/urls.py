from django.urls import path
from .views import *


# for image and file upload
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # path('products/add/', productAdd),
    # path('products/', AllProducts),
    # path('product/delete/<int:id>/', DeleteProduct, name = 'delete_product'),
    # path('product/update/<int:id>/', UpdateProduct, name = 'update_product'), 
    
    path('products/add/', ProductsAddView.as_view()), 
    path('products/', ProductListView.as_view()), 
    path('product/delete/<int:id>/', ProductDeleteView.as_view(), name = 'delete_product'),
    path('product/update/<int:id>/', ProductUpdateView.as_view(), name = 'update_product'), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)