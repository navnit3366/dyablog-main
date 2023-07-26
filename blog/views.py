from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.http import HttpRequest
from django.http.response import HttpResponseBase
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.safestring import SafeText
from django.utils.text import slugify

from .forms import BlogForm, CommentForm
from .models import BlogPost

# Create your views here.


def index(request: HttpRequest) -> HttpResponseBase:
    return render(
        request,
        "blog/post_index.html",
        {"data": BlogPost.objects.order_by("-pub_date")},
    )


def post(request: HttpRequest, blogpost_slug: SafeText) -> HttpResponseBase:
    if request.method == "POST" and request.user.has_perm(
        "blog.add_commentpost"
    ):
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)

            new_comment.parent_post = get_object_or_404(
                BlogPost, slug=blogpost_slug
            )
            new_comment.author = request.user
            new_comment.timestamp = datetime.now()
            new_comment.save()

            return redirect("blog:post", blogpost_slug=blogpost_slug)
    selected_post = get_object_or_404(BlogPost, slug=blogpost_slug)
    return render(request, "blog/view_post.html", {"post": selected_post})


@permission_required("blog.add_blogpost")
def new_post(request: HttpRequest) -> HttpResponseBase:
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)

            potential_slug = slugify(form.cleaned_data["title"])
            slug_suffix = 0
            while BlogPost.objects.filter(slug=potential_slug).count():
                slug_suffix += 1
                potential_slug = slugify(
                    f"{form.cleaned_data['title']} {slug_suffix}"
                )
            new_post.slug = potential_slug
            new_post.author = request.user
            new_post.pub_date = datetime.now()
            new_post.save()

            return redirect("blog:post", blogpost_slug=new_post.slug)
        else:
            return render(request, "blog/edit_post.html", {"form": form})
    else:
        form = BlogForm()
        return render(request, "blog/edit_post.html", {"form": form})


@permission_required("blog.change_blogpost")
def edit_post(
    request: HttpRequest, blogpost_slug: SafeText
) -> HttpResponseBase:
    selected_post = get_object_or_404(BlogPost, slug=blogpost_slug)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=selected_post)
        if form.is_valid():
            form.save()
        return redirect("blog:post", blogpost_slug=selected_post.slug)
    else:
        form = BlogForm(instance=selected_post)
        return render(
            request,
            "blog/edit_post.html",
            {"post": selected_post, "form": form},
        )
