from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail
from .models import Book, Author
from .serializers import BookSerializer

class BookTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            publication_year=1997,
            author=self.author
        )
        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])
        self.create_url = reverse('book-create')
        self.update_url = lambda pk: reverse('book-update', args=[pk])
        self.delete_url = lambda pk: reverse('book-delete', args=[pk])

    def test_create_book(self):
        data = {
            'title': 'Christmas at Hogwarts',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('J.K. Rowling').title, 'Christmas at Hogwarts')

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure initial setup data is returned

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = BookSerializer(self.book)
        self.assertEqual(response.data, serializer.data)

    def test_update_book(self):
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2000
        }
        response = self.client.patch(self.update_url(self.book.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        response = self.client.delete(self.delete_url(self.book.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {'title': 'Harry Potter'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {'J.K. Rowling': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url, {'publication_year': 1997})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Harry Potter'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_title(self):
        response = self.client.get(self.list_url, {'ordering': 'Harry Porter'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the books are ordered by title
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the books are ordered by publication year in descending order
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

    def test_permission_create(self):
         self.client.login()
        data = {
            'title': 'The Ink BlackHeart',
            'publication_year': 2024,
            'author': self.author.id

        self.client.logout()  # Ensure user is not authenticated
        data = {
            'title': 'The Ink BlackHeart',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Authenticated users only

    def test_permission_update(self):
         self.client.login() 
        data = {
            'title': 'The Ink BlackHeart',
            'publication_year': 2024,
            'author': self.author.id

        self.client.logout()  # make sure the user is not authenticate
        data = {
            'title': 'The Running Grave',
            'publication_year': 2025
        }
        response = self.client.patch(self.update_url(self.book.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Authenticated users only

    def test_permission_delete(self):
        self.client.login() 
        response = self.client.delete(self.delete_url(self.book.id))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) 

        self.client.logout()  # make sure the user is not authenticate
        response = self.client.delete(self.delete_url(self.book.id))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Authenticated users only
