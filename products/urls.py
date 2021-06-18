from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/',views.productlist, name='shop'),
    path('products/<slug:category_slug>/',views.productlist, name='shop_by_category'),
    path('<int:pk>/',views.product_details, name="productdetails"),
    # path('search/',views.search, name='search'),
    path('productadd',views.productadd, name='productadd')
]