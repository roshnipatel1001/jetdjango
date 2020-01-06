from django.contrib import admin
from .models import Author, Book
from jet.admin import CompactInline

admin.site.register(Author)
admin.site.register(Book)


class StateAuthorsInline(admin.TabularInline):
    model = Author
    extra = 1
    show_change_link = True


class StateBooksInline(CompactInline):
    model = Book
    extra = 1
    show_change_link = True


class StateAdmin(admin.ModelAdmin):
    inlines = (StateAuthorsInline, StateBooksInline)
