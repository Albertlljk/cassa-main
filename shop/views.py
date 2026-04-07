from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import Category,Product
from django.db.models import Q
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm

def product_list(request,category_slug=None):
    Category =None
    if request.path =='/':
        products = Product.objects.filter(
            available=True,
            is_popular=True
        ).order_by('name')[:4]

        return render(request, 'shop/product/list.html',{
            'category': None,
            'products': products
        })
    
    if category_slug:
        category=get_list_or_404(Category,slug=category_slug)
        products =Product.objects.filter(
            available=True,
            category=category)
        query=request.GET.get('q','').strip()
        if query:
            products = products.filter(
                Q(name__icontains=query)|
                Q(description__icontains=query))
            products=products.order_by('name')
            return render(request, 'shop/product/list.html',{
                'category': category,
                'products':products,
                'query':query,
            })


    products = Product.objects.filter(available=True)

    query = request.GET.get('q', '').strip()
    sort = request.GET.get('sort')

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    if sort == 'price_asc':
        products = products.order_by('price')

    elif sort == 'price_desc':
        products = products.order_by('-price')

    elif sort == 'name_asc':
        products = products.order_by('name')

    elif sort == 'name_desc':
        products = products.order_by('-name')

    else:
        products = products.order_by('name')

    paginator = Paginator(products, 20)

    page_number = request.GET.get('page')

    products = paginator.get_page(page_number)

    return render(request, 'shop/product/catalog.html', {
        'products': products,
        'query': query,
        'current_sort': sort,
    })

def product_detail(request, id, slug):
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True
    )

    cart_product_form = CartAddProductForm()

    return render(
        request,
        'shop/product/detail.html',
        {
            'product': product,
            'cart_product_form': cart_product_form
        }
    )