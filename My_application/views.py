from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request,"shop/index.html")

def home(request):
    return render(request,"shop/home.html")

def products(request):
    products=product.objects.filter(status=0)
    return render(request,'shop/layouts/products.html',{"product":products})


def products_details(request,pname):
    if(product.objects.filter(name=pname,status=0)):
       products=product.objects.filter(name=pname,status=0).first()
       return render(request,"shop/layouts/products_details.html",{"product":products})
    else:
        messages.error(request,"no product found")
        return redirect("products")
       
