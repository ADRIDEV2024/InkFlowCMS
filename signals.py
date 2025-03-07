from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment, Post

@receiver(post_save, sender=Comment)
def notify_post_author(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        author = post.author
        message = f"Nuevo comentario en tu post '{post.title}' por {instance.user.username}."
        author.notifications.create(message=message)
