"""newsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('product/<slug:product_category>', views.product,name="product"),
    path('productDetail/<slug:product_id>', views.productDetail,name="productDetail"),
    path('carts', views.cart,name="carts"),
    path('login', views.login,name="login"),
    path('logout', views.logout,name="logout"),
    path('register', views.register,name="register"),
    path('pay', views.pay,name="pay"),
    path('carts/addcart', views.addCart,name="addcart"),
    path('carts/updatecart', views.updateCart,name="updatecart"),
    path('carts/deletecart', views.deleteCart,name="deletecart"),
    path('customer/updatecustomer', views.updateAddressAndPhoneCustomer,name="updateCustomer"),
     path('cart/pay', views.thanhToan,name="thanhToan"),
    #path('register', views.register,name="registerCretate"),
    #path('login', views.loginPost,name="loginPost"),
]
