from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path("book/", views.BookListView.as_view(), name= "Books"),
    path("book/<int:pk>/", views.BookDetailView.as_view, name= "details" ),
]
