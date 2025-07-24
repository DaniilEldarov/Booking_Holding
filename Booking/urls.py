from django.urls import path,include
from .views import main_page,detail_products

urlpatterns = [
    path('',main_page,name='main_pge'),
    path('detail_product/<int:product_id>',detail_products, name='detail_page'),
]
