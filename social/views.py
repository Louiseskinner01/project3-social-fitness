from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm, CommentForm, CustomUserCreationForm
from .models import Post, Comment, Like

def custom_404(request, exception):
    return HttpResponse('Hey there, page not found', status=404)

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
    login_url = "login"                      # sends non-users to the login page


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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("feed")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

@login_required
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        messages.success(request, "Comment added!")
    else:
        messages.error(request, "Could not add comment.")    

    return redirect("feed")

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated!")
            return redirect("feed")  # or "profile"
        messages.error(request, "Please correct the error below.")
    else:
        form = CommentForm(instance=comment)

    return render(request, "social/edit_comment.html", {"form": form, "comment": comment})


@login_required
@require_POST
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
#Sample code from chatGPT below 
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()

    return redirect(request.META.get("HTTP_REFERER", "feed"))    