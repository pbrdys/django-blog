from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
# PostAdmin inherits from SummernoteModelAdmin
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
# admin.site.register(Post)
# NOTE: After we added class PostAdmin and registered with a decorator:
# @admin.register(Post), we can remove the line admin.site.register(Post)
admin.site.register(Comment)