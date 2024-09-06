from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.http import HttpResponseForbidden
from .forms import ExampleForm



@permission_required('bookshelf.can_view', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        #hadling the book editing logic 
        pass
        return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception= True)
def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'view_book.html', {'book': book})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if not request.user.has_perm('bookshelf.can_edit'):
        return HttpResponseForbidden("Opps! you not have permission to edit this book.")

@permission_required('bookshelf.can_view', raise_exception= True)
def book_list(request,pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_list.html', {'book': book})

#correcting way to filter data securely
books= Book.objects.filter(title_icontains=request.GET.get('search',''))



def home(request):
    return render(request, 'home.html', {})
