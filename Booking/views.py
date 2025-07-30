from django.contrib import messages
from .models import *
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


def detail_products(request,product_id):
    product=Product.objects.get(id=product_id)
    recomendated_products=Product.objects.filter(category=product.category,is_active=True,city=product.city).exclude(id=product.id)
    feedbacks=Feedback.objects.filter(product=product)
    return render(request,"main/detail_product.html",{'product':product,'recomendated_products':recomendated_products,'feedbacks':feedbacks})


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
    product=Product.objects.get(id=product_id)
    favorite_exist=Favorite.objects.filter(user=request.user ,product=product).first()
    if favorite_exist:
        favorite_exist.delete()
    else:
        product= get_object_or_404(Product,id=product_id)
        favorite=Favorite(user=request.user,product=product)
        favorite.save()
        print("cool")
    return redirect('main_page')

def favorite_list(request):
    if not request.user.is_authenticated:
        messages.error(request,"You are not logged in")
        return redirect('login')

    favorites=Favorite.objects.filter(user=request.user).order_by('-id')

    return render(request,'main/favorite_list.html',{'favorites':favorites})


def reply_on_comment(request,comment_id):
    feedback=Feedback.objects.filter(id=comment_id).first()
    if feedback:
        if request.method == 'POST':
            comment=request.POST['comment']
            feedback_response=FeedbackResponse(comment=comment,user=request.user,feedback=feedback)
            feedback_response.save()
            messages.success(request,"Thank You for your comment")

    return redirect('detail_page',product_id=feedback.product.id)

def delete_comment(request,comment_id,product_id):
    if request.method == 'POST':
        feedback=Feedback(id=comment_id)
        feedback.delete()
        messages.success(request,"Thank You for your comment")
    return redirect('detail_page',product_id=product_id)

def delete_reply(request,comment_id,product_id):
    if request.method == 'POST':
        feedback_reply=FeedbackResponse(id=comment_id)
        feedback_reply.delete()
        messages.success(request,"Thank You for your comment")
    return redirect('detail_page',product_id=product_id)