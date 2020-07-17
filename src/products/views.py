from django.shortcuts import render, get_object_or_404, Http404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object' : obj
    }
    return render(request,"products/product_detail.html",context)

def product_update_view(request,my_id):
    # initial_data = {
    #     'title' : "hey you"
    # }
    obj = Product.objects.get(id=my_id)
    form = ProductForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request,"products/product_create.html",context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request,"products/product_create.html",context)

def dynamic_lookup_view(request,my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product,id=my_id)
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        "object" : obj
    }
    return render(request,"products/product_detail.html",context)
    
def product_delete_view(request,my_id):
    obj = get_object_or_404(Product,id=my_id)
    if request.method == "POST": # to confirm the delete 
        obj.delete() 
        return redirect("../../")

    context = {
        "object" : obj
    }
    return render(request,"products/product_delete.html",context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list" : queryset  
    }
    return render(request,"products/product_list.html",context)    