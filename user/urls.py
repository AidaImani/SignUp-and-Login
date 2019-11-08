from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('signup', views.signup, name='signup'),
    path('verify/<uid>', views.verify, name='verify'),
    path('list', views.listofuser, name='list_of_user'),
]
