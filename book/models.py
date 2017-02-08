# coding: utf-8

from urlparse import urljoin
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta(object):
        app_label = 'category'
        db_table = 'category'
        verbose_name = verbose_name_plural = u'分类'

class Book(models.Model):

    title = models.CharField(max_length=50)
    avatar = models.CharField(max_length=255)
    info = models.TextField()
    author = models.CharField(max_length=50)
    category_id = models.IntegerField()
    book_update_time = models.DateTimeField()
    crawl_url = models.CharField(max_length=255)
    status = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    @property
    def category(self):
        return Category.objects.get(id=self.category_id)

    @property
    def avatar_url(self):
        return urljoin('http://7xj219.com1.z0.glb.clouddn.com', self.avatar)

    @property
    def latest_chapter(self):
        chapter_list = Chapter.objects.filter(book_id=self.id).order_by('-serial_num')
        if chapter_list:
            return chapter_list[0]

        return None

    @classmethod
    def get_recommend_book_by_category(cls, category):
        category = Category.objects.get(name=category)
        return Book.objects.filter(category_id=category.id)[:4]

    @classmethod
    def get_books_by_category_id(cls, category_id, start, count):
        end = start + count
        books = Book.objects.filter(category_id=category_id).all()[start: end]
        return books

    @classmethod
    def get_books_count_by_category_id(cls, category_id):
        return Book.objects.filter(category_id=category_id).count()

    @classmethod
    def search_books(cls, query, start, count):
        end = start + count
        return Book.objects.filter(title__contains='%s' % query)[start: end]

    @classmethod
    def search_count(cls, query):
        return Book.objects.filter(title__contains='%s' % query).count()

    class Meta(object):

        app_label = 'book'
        db_table = 'book'
        verbose_name = verbose_name_plural = u'图书'


class Chapter(models.Model):

    title = models.CharField(max_length=50)
    book_id = models.IntegerField()
    category_id = models.IntegerField()
    chapter_path = models.CharField(max_length=255)
    serial_num = models.IntegerField()
    crawl_url = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # @property
    # def content(self):
    #     return Content.objects.get(id=self.content_id).format_content

    @property
    def content(self):
        with open(self.chapter_path) as f:
            content = f.read()

        return content.replace('    ', '<br>    ')

    @classmethod
    def get_the_latest_chapter_by_book(cls, book_id):
        chapters = Chapter.objects.filter(book_id=book_id).order_by('-serial_num')
        if chapters:
            return chapters[0]

        return None

    @classmethod
    def get_chapter_count_by_book(cls, book_id):
        return Chapter.objects.filter(book_id=book_id).count()

    @classmethod
    def get_chapters(cls, book_id, start, count):
        end = start + count
        return Chapter.objects.filter(book_id=book_id).all()[start: end]

    class Meta:

        app_label = 'chapter'
        db_table = 'chapter'


# class Content(models.Model):
#
#     content = models.TextField()
#     create_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)
#
#     @property
#     def format_content(self):
#         return self.content.encode('utf-8').replace('    ', '<br>    ')
#
#     class Meta:
#
#         app_label = 'content'
#         db_table = 'content'
