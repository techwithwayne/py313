from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post'),
    path('about/', views.about, name='blog-about'),
]
