from django.contrib import admin
from django.utils.html import format_html
from .models import Page, PageView


@admin.action(description="Publicar páginas seleccionadas")
def publish_pages(modeladmin, request, queryset):
    queryset.update(is_published=True)

@admin.action(description="Despublicar páginas seleccionadas")
def unpublish_pages(modeladmin, request, queryset):
    queryset.update(is_published=False)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','preview_link' 'is_published', 'updated_at')
    list_filter = ('is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    actions = [publish_pages, unpublish_pages]
    readonly_fields = ('updated_by',)  # Evita cambios manuales en admin

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user  
        super().save_model(request, obj, form, change)
        
    def preview_link(self, obj):
        url = f"/pages/{obj.slug}/"
        return format_html(f'<a href="{url}" target="_blank">Ver página</a>')
    preview_link.short_description = "Previsualizar"



admin.site.register(Page, PageAdmin)
admin.site.register(PageView)
