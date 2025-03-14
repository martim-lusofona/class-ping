from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    path("class_attendance/", include("class_attendance.urls", namespace="class_attendance")),
    path("authentication/", include("authentication.urls")),
    path("", include("class_attendance.urls",  namespace="class_attendance_root")),
    path("qr-code/", include("qr_code.urls", namespace="qr_code")),
    path('accounts/', include('allauth.urls')),
]

if os.getenv("DEBUG") == "True":
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root= settings.MEDIA_ROOT,
)

handler404 = 'class_attendance.views.error_view'
handler500 = 'class_attendance.views.error_view'
