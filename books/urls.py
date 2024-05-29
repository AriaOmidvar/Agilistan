from django.urls import path
from .views import index, filter_books, add_book

urlpatterns = [
    path('', index, name='index'),
    path('filter/', filter_books, name='filter_books'),
    path('add/', add_book, name='add_book'),
]