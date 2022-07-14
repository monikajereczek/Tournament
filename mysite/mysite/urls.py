from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('', include('tournament.urls')),
    path('admin/', admin.site.urls),
]
