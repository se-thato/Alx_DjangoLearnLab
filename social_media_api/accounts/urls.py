from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name= 'login'),
    path('profile/', views.profile, name= 'profile'),
]
