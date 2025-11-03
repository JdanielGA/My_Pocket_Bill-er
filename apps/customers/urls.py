# apps/customers/urls.py
from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [

    # Home page
    path('', views.CustomerHomeView.as_view(), name='home'),

    # Customer CRUD URLs
    path('add/', views.CustomerCreateView.as_view(), name='add'),
    path('customers/', views.CustomerListView.as_view(), name='list'),
    path('customer/<slug:slug>/', views.CustomerDetailView.as_view(), name='detail'),
    path('customer/<slug:slug>/edit/', views.CustomerUpdateView.as_view(), name='edit'),
    path('customer/<slug:slug>/delete/', views.CustomerDeleteView.as_view(), name='delete'),
]