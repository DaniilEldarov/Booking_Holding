from django.urls import path,include
from .views import main_page,detail_products,register_view,login_user,logout_user,favorite,comments

urlpatterns = [
    path('',main_page,name='main_page'),
    path('detail_product/<int:product_id>',detail_products, name='detail_page'),
    path('register/', register_view, name='register'),
    path('login/', login_user , name='login' ),
    path('logout/', logout_user, name='logout' ),
    path('favorite/<int:product_id>', favorite, name='favorite' ),
    path('comments/', comments, name='comments' ),
]
