from django.contrib import admin
from django.urls import path
from django.urls import include
# Временный view
from odessa_courtyards.views import MemberRequestCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('odessa_courtyards.urls')),
    path('odessa_courtyards/', include('odessa_courtyards.urls')),

    # временная маршрутизация
    path('form/', MemberRequestCreate.as_view())
]
