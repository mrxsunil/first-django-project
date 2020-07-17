from django.contrib import admin

# Register your models here.
from .models import Product   # doing a relative import 

admin.site.register(Product)    # to view it on the admin page
