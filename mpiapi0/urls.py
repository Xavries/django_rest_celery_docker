from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mpiapi0 import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    #path('posts/<int:pk>/save_upvote',views.save_upvote,name='save_upvote'),
    path('posts/<int:pk>/action_view',views.action_view,name='action_view'),
]

urlpatterns = format_suffix_patterns(urlpatterns)