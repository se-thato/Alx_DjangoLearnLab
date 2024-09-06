from django.urls import path
from . import views
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path("Book/", views.BookListCreate.as_view(), name= "book"),
    path("Book/<int:pk>/", views.BookRetrieveUpdateDestroy.as_view(), name= "update"),
    path("", include("router.urls")),
]


from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]