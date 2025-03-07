from rest_framework import generics
from .models import Page
from .serializers import PageSerializer

class PageListView(generics.ListAPIView):
    queryset = Page.objects.filter(is_published=True)
    serializer_class = PageSerializer

class PageDetailView(generics.RetrieveAPIView):
    queryset = Page.objects.filter(is_published=True)
    serializer_class = PageSerializer
    lookup_field = 'slug'
