from django.contrib import admin

# Register your models here.
from product.models import Category, Note, Files


class NoteFileInline(admin.TabularInline):
    model = Files
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['status','category']
    inlines = [NoteFileInline]


class FilesAdmin(admin.ModelAdmin):
    list_display = ['title', 'note', 'file']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Note,NoteAdmin)
admin.site.register(Files,FilesAdmin)