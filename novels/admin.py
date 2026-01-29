from django.contrib import admin
from .models import Novel, Bookmark

class NovelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    search_fields = ('title', 'author')
    list_filter = ('genre',)

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'novel', 'created_at')
    search_fields = ('user__username', 'novel__title')

admin.site.register(Novel, NovelAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
