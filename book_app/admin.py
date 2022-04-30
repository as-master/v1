from django.contrib import admin
from .models import Book, Author, PublishingOffice
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(PublishingOffice)

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['title', 'rating', 'price',]
#     list_editable = ['currency']
#     list_per_page = 10