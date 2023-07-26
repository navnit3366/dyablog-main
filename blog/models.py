from django.contrib.auth.models import User
from django.db import models
from django_editorjs_fields import EditorJsJSONField

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField("Blogpost Title", max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(
        "Blogpost Description", max_length=240, blank=True
    )
    body = EditorJsJSONField(
        plugins=[
            "@editorjs/image",
            "@editorjs/header",
            "editorjs-github-gist-plugin",
            "@editorjs/code@2.6.0",  # version allowed :)
            "@editorjs/list@latest",
            "@editorjs/inline-code",
            "@editorjs/table",
        ]
    )
    pub_date = models.DateTimeField("Publication Date")
    slug = models.SlugField("Blogpost Slug", null=False, unique=True)

    def __str__(self) -> str:
        return self.title


class CommentPost(models.Model):
    parent_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    timestamp = models.DateTimeField("Time of Comment")
    body = models.TextField("Body of Comment", max_length=800)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self) -> str:
        return f"Comment by {self.author.username} on {self.parent_post.slug}"
