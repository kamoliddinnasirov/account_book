from django.urls import path, include
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login_s'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
]