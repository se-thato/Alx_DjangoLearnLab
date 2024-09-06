from django import forms


class SearchForm(forms.Form):
    search_term = forms.CharField(max_lenght=100, required=True)

#using the form to validate inputs   
def search_books(request):
    form = Search(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__incontains=query)
    else:
        books = Book.objects.all()
        return render(request, 'books/search_results.html', {'books': books, 'form': form})

def ExampleForm(request):
        form = Search(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__incontains=query)
