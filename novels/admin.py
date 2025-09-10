from django.contrib import admin
from .models import Novel

class NovelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    search_fields = ('title', 'author')
    list_filter = ('genre',)

admin.site.register(Novel, NovelAdmin)
