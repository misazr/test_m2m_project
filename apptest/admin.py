from django.contrib import admin

from apptest.models import *

# Register your models here.
admin.site.register(Author)

admin.site.register(Entry)

admin.site.register(EntryAuthors)
