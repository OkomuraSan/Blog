
from django.contrib import admin
from django.urls import path, include
from articles.views import posts
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls', namespace="blog")),
    path('blog/', include('articles.urls', namespace="blog")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('posts/', include('posts.urls', namespace="posts")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)