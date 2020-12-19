from django.urls import path
from django.contrib import admin
from .views.home import Index
from .views.login import login, logout
from .views.signup import Signup
from .views.cart import Cart
from .views.contact import Contactview
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.search import Search
from .middlewares.auth import auth_middleware
from .views import search
from django.contrib.flatpages import views

admin.site.site_header = "Welcome to Manish's Dashboard"
admin.site.site_title = "Login to Manish's Dashboard"
admin.site.index_title = "Welcome to this Portal"

app_name = 'store'
urlpatterns = [
    path('',Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('search', Search.as_view(), name='search'),
    path('contactview', Contactview.as_view(), name='contactview'),
    path('autocomplete', search.autocomplete, name='autocomplete'),
    path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
]
