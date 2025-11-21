from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy



class UserRegisterView(CreateView):
    form_class=UserRegisterForm
    template_name='registration/signup.html'
    # success_url=reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('profile_panel')

    def form_valid(self, form):
        response=super().form_valid(form)
        login(self.request,self.object)
        messages.success(self.request,f"کاربر {self.object.phone}با موفقیت ثبت نام شد")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request,"اطلاعات معتبر نیست")
        return super().form_invalid(form)

class UserLoginView(LoginView):
    template_name='registration/login.html'
    
    def get_success_url(self):
        return reverse_lazy('profile_panel')

  
    def form_valid(self, form):
        messages.success(self.request,"با موفقیت وارد شدید")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"اطلاعات نامعتبر است")
        return super().form_invalid(form)

class UserLogoutView(LogoutView):
    template_name='registration/logged_out.html'
    next_page=reverse_lazy('home')
    http_method_names = ['get', 'post']

    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request,"با موفقیت خارج شدید")
        return super().dispatch(request, *args, **kwargs)