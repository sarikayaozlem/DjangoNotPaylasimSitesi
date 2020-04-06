from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
#from django.utils.safestring import mark_safe



class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    file = models.FileField(blank=True, upload_to='files/')
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def file_tag(self):
        if self.file:
            return mark_safe('<img src="{}" height="50"/>'.format(self.file.url))
        else:
            return 'No Image'
    file_tag.short_description = 'File'



class Files(models.Model):
    note = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    file = models.FileField(blank=True, upload_to='files/')

    def __str__(self):
        return self.title