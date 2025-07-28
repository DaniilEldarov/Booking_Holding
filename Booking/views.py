from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def main_page(request):
    products=Product.objects.all()
    categories=Category.objects.filter(parent_category__isnull=True)
    liked_product_ids = []
    if request.user.is_authenticated:
        liked_product_ids = Favorite.objects.filter(user=request.user).values_list('product_id', flat=True)
    in_category="Home"
    print(request.POST)
    if request.method == 'POST':
            category_name=request.POST['category_name']
            searched_category=Category.objects.filter(title=category_name).first()
            categories=Category.objects.filter(parent_category=searched_category)
            products=Product.objects.filter(category=searched_category,is_active=True)
            in_category=searched_category
            return render(request,
                        'main/index.html',
                        {'categories':categories,
                         'products':products,
                         'in_category':in_category,
                         'liked_products': liked_product_ids,}
                        )
    return render(request,
    'main/index.html',
    {'products':products,
     'categories':categories,
     'in_category':in_category,
     'liked_products': liked_product_ids,}
    )

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully and logged in')
            return redirect('main_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})


def detail_products(request,product_id):
    product=Product.objects.get(id=product_id)
    categories=Category.objects.filter(title=product.category.title)
    if len(Feedback.objects.all())<8:
        x=len(Feedback.objects.all())
    else:
        x=8
    feedbacks=Feedback.objects.filter(product=product)
    return render(request,"main/detail_product.html",{'product':product,'categories':categories,'feedbacks':feedbacks})

def login_user(request):
    if request.method == 'POST':
        user = authenticate(email=request.POST['email'],password=request.POST['password'])
        if user:
            login(request, user)
            messages.success(request, 'Account logged in')
            return redirect('main_page')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'user/login.html',{'form':AuthenticationForm()})

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('main_page')

def comments(request):
    if request.method == 'POST':
        comment=request.POST['comment']
        product_title=request.POST['product_title']
        product=Product.objects.get(title=product_title)
        product_id=product.id
        feedback=Feedback(comment=comment,product=product,user=request.user,)
        feedback.save()
        return redirect('detail_page',product_id=product_id)
    return render(request)

def favorite(request,product_id):
    favorite_exist=Favorite.objects.filter(user=request.user ,product_id=product_id).first()
    if favorite_exist:
        favorite_exist.delete()
    else:
        product= get_object_or_404(Product,id=product_id)
        favorite=Favorite(user=request.user,product=product)
        favorite.save()
    return redirect('main_page')

