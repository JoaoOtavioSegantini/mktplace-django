from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='login_register'),
    path('login/', auth_views.LoginView.as_view(next_page='/'), name='login'),
    path('register/success', views.register_success,
         name='login_register_success'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]
