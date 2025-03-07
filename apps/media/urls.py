from django.urls import path
from .views import MediaListView, upload_media, media_by_category
from .api import MediaListView, MediaUploadView

urlpatterns = [
    path('', MediaListView.as_view(), name='media-list'),
    path('api/media/', MediaListView.as_view(), name='api-media-list'),
    path('api/media/upload/', MediaUploadView.as_view(), name='api-upload-media'),
    path('upload/', upload_media, name='upload-media'),
    path('category/<int:category_id>/', media_by_category, name='media-by-category'),
]
