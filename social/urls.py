from django.urls import path
from .views import landing, profile, PostList, create_post, delete_post, signup
from . import views

urlpatterns = [
    path("", landing, name="landing"),
    path("feed/", PostList.as_view(), name="feed"),
    path("profile/", profile, name="profile"),
    path("posts/new/", create_post, name="create_post"),
    path("posts/<int:post_id>/delete/", delete_post, name="delete_post"),
    path("signup/", signup, name="signup"),
    path("posts/<int:post_id>/comment/", views.add_comment, name="add_comment"),
    path("comments/<int:comment_id>/edit/", views.comment_edit, name="comment_edit"),
    path("posts/<int:post_id>/like/", views.toggle_like, name="toggle_like"),

]

