from .views import main_page,detail_products,favorite,comments,favorite_list
from django.urls import path
urlpatterns = [
    path('',main_page,name='main_page'),
    path('detail_product/<int:product_id>',detail_products, name='detail_page'),
    path('favorite/<int:product_id>', favorite, name='favorite' ),
    path('comments/', comments, name='comments' ),
    path('favorite_list/', favorite_list, name='favorite_list' ),
]
