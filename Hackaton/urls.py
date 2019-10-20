from django.contrib import admin
from django.urls import path
from django.urls import include
# Временный view
from odessa_courtyards.views import MemberRequestCreate, FormBeforeCreate, FormAfterCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('odessa_courtyards.urls')),
    path('api/', include('odessa_courtyards.urls')),
    # временная маршрутизация
    path('member-request', MemberRequestCreate.as_view()),
    path('form-before', FormBeforeCreate.as_view()),
    path('form-after-create', FormAfterCreate.as_view())
]
