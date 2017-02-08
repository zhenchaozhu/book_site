# coding: utf-8

from django.conf.urls import include, url
from django.contrib import admin
from book import urls as book_urls
from django.conf.urls import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'book_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(book_urls)),
]
