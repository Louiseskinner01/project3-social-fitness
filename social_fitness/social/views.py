from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):
 posts = Post.objects.all().order_by("-created_at")
 return render(request, "social/index.html",  {"posts": posts})

def post(request):
 posts = Post.objects.all().order_by("-created_at")
 return render(request, "social/create_post.html",  {"posts": posts})
