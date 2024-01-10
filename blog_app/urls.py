from django.urls import path
from .views import create_post, view_posts, delete_post

urlpatterns = [
    path('', create_post),
    path('all-posts/', view_posts, name="posts"),
    path('delete_post/<int:id>/', delete_post, name="delete_post")
]
