from typing import Any

from django import forms

from blog.models import BlogPost, CommentPost


class BlogForm(forms.ModelForm[Any]):
    class Meta:
        model = BlogPost
        fields = ["title", "description", "body"]


class CommentForm(forms.ModelForm[Any]):
    class Meta:
        model = CommentPost
        fields = ["body"]
        exclude = ["author", "timestamp", "parent_post"]
