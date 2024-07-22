from django.contrib import admin
from django.urls import path, include

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('generator/', include('generator.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
]
