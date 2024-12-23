from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("patient_user/", include("patient_user.urls")),
    path("api/", include("api.urls")),
]
