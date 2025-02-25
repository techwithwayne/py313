from django.urls import path
from .views import PostListView
""" the (.) represents the current directory """
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about')
]
