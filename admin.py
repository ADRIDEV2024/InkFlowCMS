import csv
from django.http import HttpResponse
from django.contrib import admin
from django.utils.html import format_html
from .models import MediaFile, MediaCategory


@admin.action(description="Exportar archivos multimedia a CSV")
def export_media_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="media_files.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Archivo', 'Subido por', 'Categoría', 'Es público', 'Fecha de subida'])
    
    for media in queryset:
        writer.writerow([media.id, media.file.url, media.uploaded_by.username, 
                         media.category.name if media.category else "Sin categoría",
                         "Sí" if media.is_public else "No", media.uploaded_at])
    
    return response


@admin.action(description="Marcar archivos como privados")
def make_private(modeladmin, request, queryset):
    queryset.update(is_public=False)

@admin.action(description="Marcar archivos como públicos")
def make_public(modeladmin, request, queryset):
    queryset.update(is_public=True)


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_by', 'is_public', 'uploaded_at')
    list_filter = ('is_public', 'uploaded_at')
    search_fields = ('file', 'uploaded_by__username')
    actions = [export_media_to_csv, make_private, make_public]

    def thumbnail_preview(self, obj):
        if obj.file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            return format_html(f'<img src="{obj.file.url}" width="50" height="50" style="border-radius:5px;"/>')
        return "No disponible"
    thumbnail_preview.short_description = "Vista previa"

admin.site.register(MediaFile, MediaFileAdmin)
admin.site.register(MediaCategory)
