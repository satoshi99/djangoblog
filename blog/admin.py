from django.contrib import admin
from .models import Tag, Post, ContentImage
from markdownx.admin import MarkdownxModelAdmin

class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentImageInline,
    ]


admin.site.register(Tag)
#admin.site.register(Post, PostAdmin)
admin.site.register(Post, MarkdownxModelAdmin)
