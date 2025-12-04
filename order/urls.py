from django.urls import path
from .views import *

urlpatterns=[
    path('cart',CartView.as_view(),name='cart'),
    path('cart/add/<int:product_id>/',AddCartView.as_view()),
    path('cart/remove/<int:cartitem_id>/',RemoveCartView.as_view(),name='remove_from_cart'),
    path('cart/checkout/',CheckOutView.as_view(),name='checkout'),
    path('payment/',PaymentView.as_view(),name='payment')
]
