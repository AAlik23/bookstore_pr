from django.urls import path
from . import views
from bookstore.views import store


urlpatterns = [
    # path('',views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout')
]