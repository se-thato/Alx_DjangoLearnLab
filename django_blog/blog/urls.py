from django.urls import path
from . import views
from .views import PostCreateView, PostListView, PostDetailView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('', views.home, name='home'),
     path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    
]



urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]


urlpatterns = [
     path('post/<int:pk>/comments/new/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='create_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]
