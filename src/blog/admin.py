from django.contrib import admin

# Register your models here.
from .models import Article   # doing a relative import 

admin.site.register(Article)    # to view it on the admin page
