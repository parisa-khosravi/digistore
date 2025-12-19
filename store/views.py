from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .models import *
from .forms import *
from accounts.models import *
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404,redirect


class HomeView(ListView):
    model=Product
    template_name='home.html'
    context_object_name = 'products'
    ordering=['-create_at']


class StoresView(ListView):
    model=Store
    template_name='stores.html'
    context_object_name='stores_list'


class StoreDetailView(DetailView):
    model=Store
    template_name='store_detail.html'
    context_object_name='stores'


class StoreCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Store
    form_class=StoreForm
    template_name = 'store_create.html'
    success_url=reverse_lazy('stores_list')
    
    def test_func(self):
        return self.request.user.is_seller
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

class ProductListView(ListView):
    model=Product
    temlate_name='home.html'
    template_name = 'product_create.html'
    context_object_name='product_list'


class ProductCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Product
    form_class=ProductForm

    def test_func(self):
        store=Store.objects.get(id=self.kwargs['pk'])
        return self.request.user == store.owner
    def form_valid(self, form):
        store=Store.objects.get(id=self.kwargs['pk'])
        form.instance.store=store
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('store_detail',kwargs={'pk':self.kwargs['pk']})


class UpdateProductStockView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        if request.user != product.store.owner:
            return HttpResponse("دسترسی غیرمجاز", status=403) #کاربر لاگین کرده و ولی ممنوعه وارد شدنش
        action = request.POST.get('action')
        quantity = int(request.POST.get('quantity', 1))
        
        if action == 'increase':
            product.stock += quantity
            product.save()        
        elif action == 'decrease':
            if product.stock >= quantity:
                product.stock -= quantity
                product.save()               
        return redirect('store_detail', pk=product.store.id)
    
    
class DeleteProductView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('stores_list')
        
    def test_func(self):
        product = self.get_object()
        return self.request.user == product.store.owner
        
    def get_success_url(self):
        product = self.get_object()
        return reverse_lazy('store_detail', kwargs={'pk': product.store.id})
