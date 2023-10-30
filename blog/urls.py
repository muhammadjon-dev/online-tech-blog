from django.contrib import admin
from django.urls import path, include
from blog import settings
from django.conf.urls.static import static

from django.contrib.auth import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_site.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    