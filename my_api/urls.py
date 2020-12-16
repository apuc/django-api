from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('user/<int:user_id>/', views.current_user, name='current_user'),
    path('reg/', views.register, name='register'),
    path('login/', views.login_page, name='login_page'),
    path('fib/<int:num>/', views.fibonacci, name='fibonacci'),
]
