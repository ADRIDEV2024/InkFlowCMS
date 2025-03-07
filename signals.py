from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserNotification

User = get_user_model()

@receiver(post_save, sender=User)
def create_welcome_notification(sender, instance, created, **kwargs):
    if created:
        UserNotification.objects.create(
            user=instance,
            message=f"¡Bienvenido {instance.username}! Tu cuenta ha sido creada."
        )
