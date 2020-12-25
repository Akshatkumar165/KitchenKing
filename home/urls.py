from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='login'),
    path('signup/',views.signup,name='signup'),
    path('products/',views.products,name='products'),
    path('logout/',views.logoutUser,name='logout'),
    path('bakeware/',views.bakeware,name='bakeware'),
    path('product_detail/<str:pk_test>/',views.product_detail,name='product_detail'),
    path('cart/',views.cart,name='cart'),
]
