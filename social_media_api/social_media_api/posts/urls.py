from django.urls import path    
from . import views
from .views import PostListCreate, PostRetriveUpdateDestroy, CommentListCreate, CommentRetriveUpdateDestroy


urlpatterns = [
    path('post/', PostListCreate.as_view(), name='post-create'),
    path('post/<int:pk>/', PostRetriveUpdateDestroy.as_view(), name='update'),
    path('comment/', CommentListCreate.as_view(), name='comment' ),
    path('comment/<int:pk>/', CommentRetriveUpdateDestroy.as_view(), name='update-comment'),
]


urlpatterns = [
    path('/follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('/unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
]