from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import *
from .forms import *
from accounts.models import *

class HomeView(ListView):
    model=Product
    template_name='home.html'
    context_object_name = 'products'
    ordering=['-create_at']

class StoresView(ListView):
    model=Store
    template_name='stores.html'
    context_object_name='store'

class StoreDetailView(DetailView):
    model=Store
    template_name='store_detail.html'
    context_object_name='stores'

class StoreCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Store
    form_class=StoreForm
    success_url=reverse_lazy('stores')
    
    def test_func(self):
        return self.request.user.role == 'seller'
    
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    
class ProductListView(ListView):
    model=Product
    temlate_name='home.html'
    context_object_name='products'
    
class ProductCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Product
    Form_model=ProductForm

    def test_func(self):
        store=Store.objects.get(id=self.kwargs['store.id'])
        return self.requset.user == store.seller
    def form_valid(self, form):
        store=Store.objects.get(id=self.kwargs['store.id'])
        form.instance.store=store
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('store_detail',kwargs={'pk':self.kwargs['store.id']})


# class SellerPanelView(LoginRequiredMixin,ListView):
#     model=Store
#     template_name='seller_panel.html'
#     context_object_name='stores'

#     def get_queryset(self):
#         if not self.request.user.is_seller:
#             messages.error(self.request,"شما فروشنده نیستید")
#         return Store.objects.filter(owner=self.request.user)
    
# class CustomerPanelView(LoginRequiredMixin,TemplateView):
#     template_name='customer_panel.html'

#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         if not self.request.user.is_customer:
#             messages.error(self.request,'شما حساب کاربری ندارد')
#         context['customer']=self.request.user
#         return context
