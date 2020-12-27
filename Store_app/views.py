from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'Store_app/index.html')

def about(request):
    return render(request,'Store_app/about.html')

def blog_detail(request):
    return render(request,'Store_app/blog-detail.html')

def blog(request):
    return render(request,'Store_app/blog.html')

def contact(request):
    return render(request,'Store_app/contact.html')

def home2(request):
    return render(request,'Store_app/home-02.html')

def product_detail(request):
    return render(request,'Store_app/product-detail.html')                    

def product(request):
    return render(request,'Store_app/product.html')

def shopping_cart(request):
    return render(request,'Store_app/shoping-cart.html')
               