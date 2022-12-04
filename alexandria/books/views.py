from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView, DetailView
from .models import Book, CopyBook


class HomeView(TemplateView):
    template_name = "books/home.html"


class BooksCatalogView(ListView):
    model = Book
    template_name = "books/bookscatalog.html"


class MyBooksView(ListView):
    model = CopyBook
    template_name = "books/mybooks.html"


class DetailBookView(DetailView):
    template_name = "books/home.html"


class AddBookView(TemplateView):
    template_name = "books/add_book.html"


class BorrowBookView(TemplateView):
    template_name = "books/home.html"


class ReturnBookView(TemplateView):
    template_name = "books/home.html"


class DeleteBookView(TemplateView):
    template_name = "books/home.html"


class RequestBookView(TemplateView):
    template_name = "books/home.html"


class ReserveBookView(TemplateView):
    template_name = "books/home.html"
