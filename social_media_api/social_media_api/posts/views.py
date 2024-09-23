from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

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
