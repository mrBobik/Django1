from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator

def books_view(request):
    template = 'books/books_list.html'
    book_objects = Book.objects.all()
    books_list = []
    for book in book_objects:
        books_list.append({'name': book.name,
                           'author': book.author,
                           'pub_date': book.pub_date,
                           })
    context = {'books': books_list}
    return render(request, template, context)

def books_date_view(request, pub_date):
    template = 'books/books_list.html'
    book_objects = Book.objects.filter(pub_date__contains=f'{pub_date}')
    # book_objects_all = Book.objects.all()
    books_list = []
    print(pub_date)
    for book in book_objects:
        books_list.append({'name': book.name,
                           'author': book.author,
                           'pub_date': book.pub_date,
                           })
    page_number = int(request.GET.get('page', 1))
    print(books_list)
    paginator = Paginator(books_list, 1)
    page = paginator.get_page(page_number)
    context = {'books': paginator.page(page_number), 'page':page}
    return render(request, template, context)