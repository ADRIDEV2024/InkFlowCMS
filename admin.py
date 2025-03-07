from django.contrib import admin
from .models import Post, Comment, Category, Tag

@admin.action(description="Publicar posts seleccionados")
def publish_posts(modeladmin, request, queryset):
    queryset.update(is_published=True)

@admin.action(description="Despublicar posts seleccionados")
def unpublish_posts(modeladmin, request, queryset):
    queryset.update(is_published=False)

@admin.action(description="Aprobar comentarios seleccionados")
def approve_comments(modeladmin, request, queryset):
    queryset.update(is_approved=True)

@admin.action(description="Rechazar comentarios seleccionados")
def reject_comments(modeladmin, request, queryset):
    queryset.update(is_approved=False)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'categories', 'tags', 'author')
    prepopulated_fields = {'slug': ('title',)}
    actions = [publish_posts, unpublish_posts]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    actions = [approve_comments, reject_comments]

admin.site.register(Category)
admin.site.register(Tag)

