from django.shortcuts import get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        Post.objects.all().delete
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostRetriveUpdateDestroy(generics.RetrieveUpdatedDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer

    def delete(self, request, *args, **kwargs):  
        Comment.objects.all().delete
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentRetriveUpdateDestroy(generics.RetrieveUpdatedDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


    def follow_user(request, username):
        #making sure the user is aunthenticated
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You need to be logged in to follow other users")

        #preventing the user to follow themselves
        if request.user.username == username:
            return HttpResponseForbidden("Opps!! you cannot follow yourself.")
        
        #getting the user to follow
        user_to_follow = get_object_or_404(User, username=username)


    def unfollow_user(request, username):
        #making sure the user is aunthenticated
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You need to be logged in to follow other users")
        

        #preventing a user from unfollowing themselves
        if request.user.username == username:
            return HttpResponseForbidden("Opps!! you cannot unfollow yourself.")

        #get the user to be able to unfollow
        user_to_unfollow = get_object_or_404(User, username=username)






from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if created:
        # Create notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )
        return JsonResponse({'message': 'Post liked'}, status=201)
    else:
        return JsonResponse({'message': 'You have already liked this post'}, status=400)

@login_required
def unlike_post(request, pk):
    post = permissions.IsAuthenticated, generics.get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return JsonResponse({'message': 'Post unliked'}, status=200)
    except Like.DoesNotExist:
        return JsonResponse({'message': 'You have not liked this post'}, status=400)