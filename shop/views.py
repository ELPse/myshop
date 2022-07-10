from django.shortcuts import render,get_object_or_404
from .models import Product,Categoty
# Create your views here.
def prduct_list(requsets,category_slug=None):
    category_slug = None
    categories = Categoty.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Categoty,slug=category_slug)
        products = products.filter(category=category)
    return render(requsets,
                  'shop/product/list.html',
                    {'category':category,'categories':categories,'products':products})


def product_detail(requests, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(requests, 'shop/product/detail.html', {'product': product})

