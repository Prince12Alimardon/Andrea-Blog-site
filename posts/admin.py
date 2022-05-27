from django.contrib import admin
from .models import Post, Category, Comment, Tag


# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'category', 'created_at')
    list_filter = ('created_at', 'category', 'tag')
    search_fields = ('title',)
    filter_horizontal = ('tag',)
    prepopulated_fields = ({'slug': ('title',)})


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
