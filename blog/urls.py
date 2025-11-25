from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_blogs, name="my_blogs"),
    path("create/", views.create_blog, name="create_blog"),
    
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("blog/edit/<int:pk>/", views.edit_blog, name="edit_blog"),
    path("blog/delete/<int:pk>/", views.delete_blog, name="delete_blog"),
]
