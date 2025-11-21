from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import FormView,TemplateView,View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.db import transaction
from .models import *
from .forms import *
from store.models import *
from accounts.models import *
from django.urls import reverse_lazy

class CartView(LoginRequiredMixin,UserPassesTestMixin,TemplateView):
    template_name='cart.html'

    def test_func(self):
        return self.request.user.is_customer
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cart,create = cart.objects.get_or_create(customer=self.request.user)
        context['cartitem']=CartItem.objects.filter(cart=cart)
        context['total_price']=sum(item.total_price for item in context['cartitem'])
        return context
    
class AddCartView(LoginRequiredMixin,UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_customer
    
    def post(self,request,product_id):
        product=get_object_or_404(Product,id=product_id)
        cart,created=Cart.objects.get_or_create(customer=request.user)
        cartitem,created=CartItem.objects.get_or_create(
            product=product,
            cart=cart,
            defaults={'quantity':1}
        )
        if not created:
            self.quantity +=1
            cartitem.save()

        messages.success(request,f"{product} به سبد خرید شما اضافه شد")
        return redirect ('home')
    
class RemoveCartView(LoginRequiredMixin,UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_customer
    def post(self,request,cartitem_id):
        cart_item=get_object_or_404(CartItem,id=cartitem_id,cart__customer=request.user)
        product_name=cart_item.product.name
        cart_item.delete()
        messages.success(request,f"{product_name}حذف شد از سبد خرید شما ")
        return redirect ('cart')
    
class CheckOutView(LoginRequiredMixin,UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_customer
    
    def post(self,request,):
        cart=get_object_or_404(Cart,customer=request.user)
        cart_items=CartItem.objects.filter(cart=cart)

        if not cart_items.exists():
            messages.error(request,'سبد خرید شما خالی است')
            return redirect('cart')
        
        total_price=sum(item.total_price for item in cart_items)

        if request.user.balance < total_price:
            messages.error(request,'موجودی کافی نیست')
            return redirect('cart')
        else:
            try:
                with transaction.atomic():
                    request.user.balance -= total_price
                    request.user.save()
                    cart_items.delete()
            except Exception as e:
                messages.error(request,'خطا در برداخت')
                return redirect('cart')

   
class PaymentView(LoginRequiredMixin,UserPassesTestMixin,FormView):
    form_class=PaymentForm
    template_name = 'payment.html'
    success_url= reverse_lazy ('customer_panel')
    def test_func(self):
        return self.request.user.is_customer
    
    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        self.request.user.balance += amount
        self.request.user.save()
        messages.success(self.request,'مبلغ مورد درخواست به کیف بول شما اضافه شد')
        return super().form_valid(form)


  



    

