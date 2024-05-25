from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import notes.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notes.views.redirect_to_home_view, name='redirect_to_home'),
    path('notes/', include('notes.urls')),
    path('accounts', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)