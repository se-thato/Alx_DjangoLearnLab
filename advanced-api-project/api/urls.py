from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookDeleteView, BookUpdateView

urlpatterns = [
    path("books/", views.BookListView.as_view(), name= "Books"),
    path("books/<int:pk>/", views.BookDetailView.as_view, name= "details" ),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]
