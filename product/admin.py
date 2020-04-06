from django.contrib import admin

# Register your models here.
from product.models import Category, Product, Files


class NoteFileInline(admin.TabularInline):
    model = Files
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'file_tag', 'status']
    readonly_fields = ('file_tag',)
    list_filter = ['status', 'category']
    inlines = [NoteFileInline]


class FilesAdmin(admin.ModelAdmin):
    list_display = ['title', 'note', 'file']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Files,FilesAdmin)