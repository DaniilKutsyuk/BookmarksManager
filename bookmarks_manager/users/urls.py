from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    # API
    path('api/login/', views.api_login_view, name='api_login'),
    path('api/register/', views.api_register_view, name='api_register'),
    path('api/logout/', views.api_logout_view, name='api_logout'),
]
