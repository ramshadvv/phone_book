from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('register',views.register,name='register'),
    path('edit/<str:pk>',views.edit,name='edit'),
    path('delete/<str:pk>',views.delete,name='delete'),
]