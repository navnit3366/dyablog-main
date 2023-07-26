# Generated by Django 4.1.1 on 2022-10-15 21:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "blog",
            "0001_squashed_0004_remove_blogpost_author_alter_blogpost__author",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="CommentPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(verbose_name="Time of Comment"),
                ),
                (
                    "body",
                    models.TextField(
                        max_length=800, verbose_name="Body of Comment"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.blogpost",
                    ),
                ),
            ],
        ),
    ]