from django.urls import path
from . import views

urlpatterns = [
    # API
    path('api/bookmarks/', views.bookmark_list_api, name='bookmark_list_api'),
    path('api/bookmarks/create/', views.create_bookmark_api, name='create_bookmark_api'),
    path('api/bookmarks/<int:pk>/', views.view_bookmark_api, name='view_bookmark_api'),
    path('api/bookmarks/<int:pk>/update/', views.update_bookmark_api, name='update_bookmark_api'),
    path('api/bookmarks/<int:pk>/delete/', views.delete_bookmark_api, name='delete_bookmark_api'),

    # Template
    path('bookmarks/', views.bookmark_list, name='bookmark_list'),
    path('bookmarks/create/', views.create_bookmark, name='create_bookmark'),
    path('bookmarks/<int:pk>/', views.view_bookmark, name='view_bookmark'),
    path('bookmarks/<int:pk>/update/', views.update_bookmark, name='update_bookmark'),
    path('bookmarks/<int:pk>/delete/', views.delete_bookmark, name='delete_bookmark'),
]
