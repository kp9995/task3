from django.shortcuts import render

from . models import Products,Images, Category
from django.core.paginator import Paginator


# Create your views here.



def index(request):
    products = Products.objects.all()[:4]
    return render(request, 'index.html', context={'products':products})


def productlist(request,category_slug=None):
    categories = Category.objects.all()
    order = '-created'
    if 'search' in request.GET:
        pass

    if category_slug:
        products = Products.objects.filter(category__slug=category_slug)
    else:
        products = Products.objects.all()

    if 'ordering' in request.GET:
        order = request.GET.get('ordering')
        products = products.order_by(order)



    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'productlist.html',context={'page_obj':page_obj,
                                                      'categories':categories})


def product_details(request,pk):

    product = Products.objects.get(pk=pk)
    images = Images.objects.filter(product=product)
    context = {
        "product":product,
        "images":images,
    }
    return render(request, 'Products_detail.html', context=context)

