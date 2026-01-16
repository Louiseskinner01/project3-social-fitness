from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post

def landing(request):
    return render(request, "social/landing.html")

@login_required
def profile(request):
    my_posts = Post.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "social/profile.html", {"posts": my_posts}) 

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = "social/index.html"      # template path
    context_object_name = "posts"            # template uses {{ posts }}
    ordering = ["-created_at"]               # displays "newest" first
    paginate_by = 6                          # display x number of posts per page
    login_url = "account_login"                      # sends non-users to the login page


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("feed")
    else:
        form = PostForm()

    return render(request, "social/create_post.html", {"form": form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    if request.method == "POST":
        post.delete()
        return redirect("profile")

    return redirect("profile")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("feed")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})