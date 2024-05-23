from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

import notes.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notes.views.redirect_to_home_view, name='redirect_to_home'),
    path('notes/', include('notes.urls')),

    path('accounts', include('django.contrib.auth.urls')),

]
