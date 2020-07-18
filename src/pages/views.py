from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Handles your various webpages 

def home_view(request, *args, **kwargs):   
    # functions an HTML code
    # return HttpResponse("<h1>Hello World</h1>") # String of HTML code 

    return render(request,"home.html",{})


def contact_view(req,*args, **kwargs):   
    print(args,kwargs)
    print(req.user)  # tell which user is requesting
    # return HttpResponse("<h1>Contact Page</h1>") # String of HTML code 
    return render(req,"contact.html",{})


def about_view(request, *args, **kwargs):   
    # functions an HTML code
    # return HttpResponse("<h1>Hello World</h1>") # String of HTML code 
    my_context = {
        # "my_text": "This is about me",
        # "my_number" : 123,
        # "my_list" : [1,2,3,4,5,5]
    }
    return render(request,"about.html",my_context)

