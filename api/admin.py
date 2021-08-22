from django.contrib import admin

from .models import Comment, Review, User, Title, Category, Genre


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'score', 'text', 'author', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date', 'author')
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review', 'text', 'author', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date', 'author')
    empty_value_display = '-пусто-'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
