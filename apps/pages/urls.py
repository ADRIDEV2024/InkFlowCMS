from django.urls import path
from .views import page_detail
from .api import PageListView, PageDetailView

urlpatterns = [
    path('api/pages/', PageListView.as_view(), name='api-pages-list'),
    path('api/pages/<slug:slug>/', PageDetailView.as_view(), name='api-pages-detail'),
    path('<slug:slug>/', page_detail, name='page-detail'),
]
