from django.shortcuts import render
from rest_framework import generics, status, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    serializer_class = UserSerializer
    filter_backends = DjangoFilterBackend
    search_fields = ['title', 'author']
    filterset_class = BookFilter
    OrderingFilter = ["title", "publication_year"]

      def create(self, serializer):
        # Custom logic before saving
        serializer.save()

      def get_queryset(self):
        return Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

      def update(self, request, *args, **kwargs):
        # Custom logic before updating
        response = super().update(request, *args, **kwargs)
        return response

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 


class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

class DeleteView(generics.DeleteAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

