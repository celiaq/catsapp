from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create-post/', views.create_post, name='create_post'),
    path('add/', views.create_post, name='add_cat_post'),
    path('view-photos/', views.view_photos, name='view_photos'),
    path('delete-photo/<int:post_pk>/', views.delete_photo, name='delete_photo'),
]
