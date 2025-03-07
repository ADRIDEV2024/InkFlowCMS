from rest_framework import generics, permissions
from .models import MediaFile
from .serializers import MediaFileSerializer

class MediaListView(generics.ListAPIView):
    queryset = MediaFile.objects.filter(is_public=True)
    serializer_class = MediaFileSerializer

class MediaUploadView(generics.CreateAPIView):
    serializer_class = MediaFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
