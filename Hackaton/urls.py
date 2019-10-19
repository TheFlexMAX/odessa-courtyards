from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('odessa_courtyards.urls')),
    path('odessa_courtyards/', include('odessa_courtyards.urls')),
]
