from django.urls import path
from .views import PostListView, PostDetailView, add_comment
from .api import PostListView, PostDetailView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('api/posts/', PostListView.as_view(), name='api-posts-list'),
    path('api/posts/<slug:slug>/', PostDetailView.as_view(), name='api-posts-detail'),
    path('api/posts/<int:post_id>/comments/', CommentCreateView.as_view(), name='api-add-comment'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/comment/', add_comment, name='add-comment'),
]
