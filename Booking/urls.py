from .views import main_page,product_list,delete_reply,detail_products,favorite,comments,favorite_list,reply_on_comment,delete_comment
from django.urls import path
urlpatterns = [
    path('',main_page,name='main_page'),
    path('detail_product/<int:product_id>',detail_products, name='detail_page'),
    path('favorite/<int:product_id>', favorite, name='favorite' ),
    path('comments/', comments, name='comments' ),
    path('favorite_list/', favorite_list, name='favorite_list' ),
    path('reply_on_comment/<int:comment_id>',reply_on_comment, name='reply_comment'),
    path('delete_comment/<int:comment_id>/<int:product_id>',delete_comment, name='delete_comment'),
    path('delete_reply/<int:comment_id>/<int:product_id>',delete_reply, name='delete_reply'),
    path('product_list/', product_list, name='product_list'),
]
