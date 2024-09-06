from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path("books/", views.BookListView.as_view(), name= "Books"),
    path("books/<int:pk>/", views.BookDetailView.as_view, name= "details" ),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
