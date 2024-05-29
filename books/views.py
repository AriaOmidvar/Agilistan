from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book
from .forms import BookForm

def filter_books(request):
    title = request.GET.get('title', '')
    publication_year = request.GET.get('publication_year', '')
    edition = request.GET.get('edition', '')
    author = request.GET.get('author', '')

    books = Book.objects.all()

    if title:
        books = books.filter(title__icontains=title)
    if publication_year:
        books = books.filter(publication_year=publication_year)
    if edition:
        books = books.filter(edition__icontains=edition)
    if author:
        books = books.filter(authors__icontains=author)

    book_list = list(books.values('title', 'publication_year', 'edition', 'authors'))
    return JsonResponse(book_list, safe=False)

def index(request):
    return render(request, 'books/index.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a page, e.g., the index page
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})
