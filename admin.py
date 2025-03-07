from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserNotification


@admin.action(description="Marcar usuarios como verificados")
def make_verified(modeladmin, request, queryset):
    queryset.update(is_verified=True)

@admin.action(description="Eliminar todas las notificaciones del usuario")
def clear_notifications(modeladmin, request, queryset):
    for user in queryset:
        user.notifications.all().delete()


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_verified', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
    actions = [make_verified, clear_notifications]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserNotification)
