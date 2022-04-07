from django.shortcuts import render
from .models import Book
from django.template import RequestContext
# Create your views here.

def show_all_books(request):
    books = Book.objects.all()
    return render(request, 'book_app/all_books.html', {
     'books': books
    })

def show_one_book(request, id_book:int):
    book = Book.objects.get(id=id_book)
    return render(request, 'book_app/one_book.html', {
     'book': book
    })