from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all-auth/', include("allauth.urls")),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("rest-framework/", include("rest_framework.urls")),
    path('app/', include("content.api.urls")),
    re_path(r"^media/(?P<path>.*)$", serve,
            {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve,
            {"document_root": settings.STATIC_ROOT}),
]
