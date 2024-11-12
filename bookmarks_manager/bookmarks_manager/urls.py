from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('bookmarks/', include('bookmarks.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', lambda request: redirect('login')),
]