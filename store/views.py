from django.shortcuts import render, get_object_or_404
from category.models import Category
from store.models import Product

# Store view function
def store(request, category_slug=None):
    categories = None
    products = None

    # If a category is selected, filter products by category
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True) 
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True)  # Fetch all available products
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }

    return render(request, 'store/store.html', context)

def product_detail(request,category_slug,product_detail):
    return render(request,'store/product_detail.html')