from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('list/', views.transaction_list, name='transaction_list'),
    path('create/', views.transaction_create, name='transaction_create'),
    path('update/<int:pk>/', views.transaction_update, name='transaction_update'),
    path('delete/<int:pk>/', views.transaction_delete, name='transaction_delete'),
    path('summary/', views.summary_view, name='summary'),
    path('register/',views. register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
  
]
