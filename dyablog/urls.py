"""dyablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import include, path

from . import settings


def redirect_to_blog(request: HttpRequest) -> (HttpResponseRedirect):
    return redirect("blog:index", permanent=False)


urlpatterns = [
    path("", redirect_to_blog),
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("editorjs/", include("django_editorjs_fields.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
