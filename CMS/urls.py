from django.urls import path, include

urlpatterns = [
    path('api/', include('users.urls')),
    path('api/', include('pages.urls')),
    path('api/', include('blog.urls')),
    path('api/', include('media.urls')),
]
