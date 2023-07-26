from django.contrib import admin

from blog.models import BlogPost, CommentPost

# Register your models here.


class AdminBlogPost(admin.ModelAdmin[BlogPost]):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(BlogPost, AdminBlogPost)


admin.site.register(CommentPost)
