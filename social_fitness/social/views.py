"""
from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):
 posts = Post.objects.all().order_by("-created_at")
 return render(request, "social/index.html",  {"posts": posts})

def post(request):
 posts = Post.objects.all().order_by("-created_at")
 return render(request, "social/create_post.html",  {"posts": posts})
"""

from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = "social/index.html"      # your template path
    context_object_name = "posts"            # so template uses {{ posts }}
    ordering = ["-created_at"]               # newest first
    paginate_by = 6   
