from django.contrib import admin
from .models import Post,Author,Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
     list_display = ("title", "author",)
     prepopulated_fields = {"slug": ("title",)}
    #  list_filter = ["author", "title"]
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
