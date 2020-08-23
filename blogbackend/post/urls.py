from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    UserListView,
    UserDetailView)

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),

]
