from django.urls import path
from .views import *
from user.views import *

urlpatterns=[
    path('register/',UserRegisterView.as_view(),name='signup'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('profile/',ProfileView.as_view(),name='profile_panel'),

]