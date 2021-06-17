from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('shop/',views.productlist, name='shop'),
    path('shop/<slug:category_slug>/',views.productlist, name='shop_by_category'),
    path('<int:pk>/',views.product_details, name="productdetails"),
]