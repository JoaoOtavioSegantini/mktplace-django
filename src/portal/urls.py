"""mktplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_products/', views.my_products, name='my_products'),
    path('product/new/', views.product_new, name='product_new'),
    path('product/new/question/<int:product_id>',
         views.product_new_question, name='product_question_new'),
    path('product/edit/<int:product_id>',
         views.product_edit, name='product_edit'),
    path('product/<str:slug>',
         views.product_show, name='product_show'),
    path('product/<int:product_id>/images',
         views.product_images, name='product_images'),
    path('product/<int:product_id>/questions',
         views.product_question, name='product_question'),
    path('product/<int:product_id>/questions/<int:question_id>',
         views.product_answer_question, name='product_answer_question'),
]
