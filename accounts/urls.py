from django.urls import path, include

from . import views

urlpatterns = [
    
    path('', views.user_home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path("update-profile-image/", views.update_profile_image, name="update_profile_image"),
    path("delete-profile-image/", views.delete_profile_image, name="delete_profile_image"),
]

