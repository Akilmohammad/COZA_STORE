from django.urls import path,include
from .views import index,about,blog_detail,contact,home2,product_detail,product,shopping_cart,blog

urlpatterns = [
    path('',index,name='index'),
    path('about',about,name='about'),
    path('blog_detail',blog_detail,name='blog_detail'),
    path('blog',blog,name='blog'),
    path('contact',contact,name='contact'),
    path('home2',home2,name='home2'),
    path('product_detail',product_detail,name='product_detail'),
    path('product',product,name='product'),
    path('shopping_cart',shopping_cart,name='shopping_cart'),
    # path('about',about,name='about'),
]