from django.urls import path
from .views import *

urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('stores/',StoresView.as_view(),name='stores_list'),
    path('store/<int:pk>',StoreDetailView.as_view(),name='store_detail'),
    path('store/create',StoreCreateView.as_view(),name='store_create'),
    path('products',ProductListView.as_view(),name='product_list'),
    path('store/<int:pk>/product/create/',ProductCreateView.as_view(),name='product_create'),
    # path('seller/', SellerPanelView.as_view(), name='seller_panel'),
    # path('customer/', CustomerPanelView.as_view(), name='customer_panel'),
]