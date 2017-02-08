# coding: utf-8

from django.shortcuts import render
from book.models import Book, Chapter, Category
from django.shortcuts import render_to_response
import qiniu

# qiniu.rs

def index(request):

    category_list = Category.objects.all()
    recommend_categories = [1, 2]
    recommend_books = []
    for category in category_list:
        recommend_books.append((category.name, category.id, Book.objects.filter(category_id=category.id)[0:4]))
    data = {
        'categories': category_list,
        'recommend_books': recommend_books,
    }
    return render_to_response('index.html', locals())


def book(request, book_id):
    page = int(request.GET.get('page', 1))
    count = int(request.GET.get('count', 6))
    start = (page - 1) * count
    book = Book.objects.get(id=book_id)
    latest_chapter = Chapter.get_the_latest_chapter_by_book(book_id)

    chapters = Chapter.get_chapters(book_id, start, count)
    total_chapters_count = Chapter.get_chapter_count_by_book(book_id)
    if page > 1:
        prev_page = page - 1

    if page * count < total_chapters_count:
        next_page = page + 1

    if total_chapters_count % count == 0:
        page_count = total_chapters_count / count
    else:
        page_count = total_chapters_count / count  + 1

    return render_to_response('book_intro.html', locals())


def chapter(request, book_id, chapter_id):

    book = Book.objects.get(id=book_id)
    chapter_count = Chapter.objects.filter(book_id=book_id).count()
    chapter = Chapter.objects.filter(id=chapter_id).first()
    chapter_num = chapter.serial_num
    if int(chapter_num) > 1:
        previous_chapter_num = int(chapter_num) - 1
        previous_chapter = Chapter.objects.filter(book_id=book_id, serial_num=previous_chapter_num).first()

    if int(chapter_num) < chapter_count:
        next_chapter_num = int(chapter_num) + 1
        next_chapter = Chapter.objects.filter(book_id=book_id, serial_num=next_chapter_num).first()

    return render_to_response('chapter.html', locals())


def book_category(request, category_id):

    page = int(request.GET.get('page', 1))
    count = int(request.GET.get('count', 6))
    start = (page - 1) * count
    category = Category.objects.get(id=category_id)
    books = Book.get_books_by_category_id(category_id, start, count)
    total_category_books = int(Book.get_books_count_by_category_id(category_id))
    has_prev_page = False
    has_next_page = False
    prev_page = 1
    next_page = 1
    if page > 1:
        has_prev_page = True
        prev_page = page - 1

    if page * count < total_category_books:
        has_next_page = True
        next_page = page + 1

    return render_to_response('category_book.html', locals())


def book_search(request):

    page = int(request.GET.get('page', 1))
    count = int(request.GET.get('count', 6))
    start = (page - 1) * count
    query = request.GET.get('query', '')
    search_books = []
    has_prev_page = False
    has_next_page = False
    prev_page = 1
    next_page = 1
    if query:
        search_books = []
        books_rst = Book.search_books(query, start, count)
        search_count = Book.search_count(query)
        if page > 1:
            has_prev_page = True
            prev_page = page - 1

        if page * count < search_count:
            has_next_page = True
            next_page = page + 1

        for book in books_rst:
            print book
            book.title = book.title.replace(query, '<span class="theWord">%s</span>' % query)
            search_books.append(book)

    return render_to_response('search_list.html', locals())