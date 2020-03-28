from django.contrib import admin

# Register your models here.
from product.models import Category, Note


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['status','category']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Note,NoteAdmin)