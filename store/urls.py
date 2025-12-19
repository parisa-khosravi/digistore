from django.urls import path
from .views import *

urlpatterns=[
    path('home/',HomeView.as_view(),name='home'),
    path('stores/',StoresView.as_view(),name='stores_list'),
    path('store/<int:pk>/',StoreDetailView.as_view(),name='store_detail'),
    path('store/create/',StoreCreateView.as_view(),name='store_create'),
    path('products/',ProductListView.as_view(),name='product_list'),
    path('store/<int:pk>/product/create/',ProductCreateView.as_view(),name='product_create'),
    path('products/<int:product_id>/update-stock/', UpdateProductStockView.as_view(),name='update_product_stock'),
     path('products/<int:pk>/delete/',DeleteProductView.as_view(), name='delete_product'),
]