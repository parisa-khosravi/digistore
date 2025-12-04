from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import *

class ProfileView(LoginRequiredMixin,UpdateView):
    form_class=ProfileForm
    # success_url=reverse_lazy('profile_panel')
    
    def get_success_url(self):
        return reverse_lazy('profile_panel')
    def get_object(self, queryset =None):
        profile,created=Profile.objects.get_or_create(user=self.request.user)
        return profile
    def get_template_names(self):
         if self.request.user.is_seller:
            return ['seller_panel.html']
         return['customer_panel.html']

       
    def form_valid(self, form):
        messages.success(self.request,'بروفایل شما با موفقیت تکمیل شد')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,'دوباره تلاش کنید')
        return super().form_invalid(form)
