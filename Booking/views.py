from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def main_page(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    return render(request,
    'main/index.html',
    {'products':products,'categories':categories}
    )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
    form=UserCreationForm()
    return render(request,
    'user/register.html',
    {'form':form}
    )


def detail_products(request,product_id):
    product=Product.objects.get(id=product_id)
    categories=Category.objects.filter(title=product.category.title)
    return render(request,"main/detail_product.html",{'product':product,'categories':categories})