from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cart/',views.tryy,name='cart'),
    path('removetotal/',views.removetotal,name='removetotal'),
    path('placeorder/',views.placeorder,name='placeorder'),
    path('checkout/',views.checkout,name='checkout'),
    path('addcart/',views.addtocart,name='addcart'),
    path('removecart/',views.removefromcart,name='removecart'),
    path('veggie/',views.veggie,name='vegetable'),
    path('offer/',views.offer,name='offer'),
    path('snack/',views.snack,name='snack'),
    path('fruit/',views.fruit,name='fruit')
  
]