from django.urls import path
from  My_application import views

urlpatterns = [
path('',views.index,name="index"),
path('home',views.home,name="home"),
path('products',views.products,name="products"),
path('products/<str:pname>',views.products_details,name="products_details"),
path('buy',views.buy,name="buy")
]