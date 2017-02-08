# coding: utf-8
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'book.views.index'),
    url(r'^book/(\d+)/$', 'book.views.book'),
    url(r'^book/category/(\d+)/$', 'book.views.book_category'),
    url(r'^book/(\d+)/chapter/(\d+)/', 'book.views.chapter'),
    url(r'^book/search/$', 'book.views.book_search'),
)