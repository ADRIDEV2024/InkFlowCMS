from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MediaFile

@receiver(post_save, sender=MediaFile)
def log_media_upload(sender, instance, created, **kwargs):
    if created:
        print(f"Archivo subido: {instance.file.name} por {instance.uploaded_by.username}")
