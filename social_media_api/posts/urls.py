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





from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/like/', views.like_post, name='like_post'),
    path('<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
]