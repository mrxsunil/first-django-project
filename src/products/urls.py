from django.contrib import admin
from django.urls import path
from  products.views import (product_create_view, product_detail_view, 
                            dynamic_lookup_view,  product_delete_view,
                            product_list_view,    product_update_view)
from pages.views import home_view,about_view,contact_view

from pages import views
app_name = "products"
urlpatterns = [
    path('<int:my_id>',dynamic_lookup_view, name='product_details_view'),
    path('<int:my_id>/delete',product_delete_view, name='product_delete_view'),
    path('<int:my_id>/update',product_update_view, name='product_update_view'),
    path('',product_list_view, name='product_list_view'),
    path('create/',product_create_view, name="product_create_view"),
]