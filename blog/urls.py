from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="blog/login.html", next_page="blog:index"
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="blog:index"),
        name="logout",
    ),
    path("new-post/", views.new_post, name="new-post"),
    path("<slug:blogpost_slug>/", views.post, name="post"),
    path("<slug:blogpost_slug>/edit/", views.edit_post, name="edit-post"),
]
