# coding: utf-8

import os
import sys
import django
from django.core.paginator import Paginator

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'book_site.settings')
django.setup()
if DIR_PATH not in sys.path:
    sys.path.append(DIR_PATH)

from book.models import Content, Chapter
def chunked_iterator(queryset, chunk_size=100):
    paginator = Paginator(queryset, chunk_size)
    for page in range(1, paginator.num_pages + 1):
        for obj in paginator.page(page).object_list:
            yield obj

for content in chunked_iterator(Content.objects.all()):
    chapter_id = content.chapter_id
    chapter = Chapter.objects.get(id=chapter_id)
    chapter.content_id = content.id
    print 'change'
    chapter.save()


# contents = Content.objects.all()
# for content in contents:
#     chapter_id = content.chapter_id
#     chapter = Chapter.objects.get(id=chapter_id)
#     chapter.content_id = content.id
#     print 'change'
#     chapter.save()