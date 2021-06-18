from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from .models import Products, Images, Category
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector
from django.forms import inlineformset_factory
from .forms import ImageAddForm, ProductAddForm

# Create your views here.


def index(request):
    products = Products.objects.all()[:4]
    return render(request, 'index.html', context={'products': products})


def productlist(request, category_slug=None, ):
    categories = Category.objects.all()
    products = Products.objects.all()
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')
    order = '-created'
    if category_slug:
        products = Products.objects.filter(category__slug=category_slug)

    if 'ordering' in request.GET:
        order = request.GET.get('ordering')
        products = products.order_by(order)
    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)
    if 'search' in request.GET:
        search_query = request.GET.get('search')
        products = Products.objects.annotate(search=SearchVector('name', 'category__name')).filter(search=search_query).order_by(order)

    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'productlist.html', context={'page_obj': page_obj,
                                                        'categories': categories})


def product_details(request, pk):
    product = Products.objects.get(pk=pk)
    images = Images.objects.filter(product=product)
    context = {
        "product": product,
        "images": images,
    }
    return render(request, 'Products_detail.html', context=context)

#
# def search(request):
#     search_query = request.GET.get('search')
#     products = Products.objects.annotate(search=SearchVector('name', 'category__name')).filter(search=search_query)
#     context = {'products': products}
#     return render(request, 'search.html', context=context)


def productadd(request):
    image_form = ImageAddForm()
    product_form = ProductAddForm()
    if request.method == 'POST':


        return redirect(reverse('products:index'))
    context = {"image_form": image_form,
               "product_form": product_form}
    return render(request, 'productadd.html', context=context)