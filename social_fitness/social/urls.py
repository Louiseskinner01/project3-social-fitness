from django.urls import path
from .views import landing, profile, PostList, create_post, delete_post, signup

urlpatterns = [
    path("", landing, name="landing"),
    path("feed/", PostList.as_view(), name="feed"),
    path("profile/", profile, name="profile"),
    path("posts/new/", create_post, name="create_post"),
    path("posts/<int:post_id>/delete/", delete_post, name="delete_post"),
    path("signup/", signup, name="signup"),
]

