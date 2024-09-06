from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django import forms


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username



class Book(models.Model):
    title = models.CharField(max_lenght=200)
    author = models.CharField(max_lenght=100)
    created_at = models.DateTimeField(auto_now = True)

    

class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]


class SearchForm(forms.Form):
    search_term = forms.CharField(max_lenght=100)

 #using the form to validate inputs   
form =SearchForm(request.GET)
if form.is_valid():
    search_term = form.cleaned_data['search_term']
    books = Book.objects.filter(title_icontains=search_term)
