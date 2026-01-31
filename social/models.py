from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    WORKOUT = [
        ("run", "RUN"),
        ("cycle", "CYCLE"),
        ("row", "ROW"),
        ("swim", "SWIM"),
        ("yoga", "YOGA"),
        ("pilates", "PILATES"),
        ("functional strength", "FUNCTIONAL STRENGTH"),
        ("other", "OTHER")
    ]
    INTENSITY = [
        ("easy", "EASY"),
        ("medium", "MEDIUM"),
        ("hard", "HARD")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to="posts/")
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    workout = models.CharField(max_length=20, choices=WORKOUT, blank=True)
    intensity = models.CharField(max_length=20, choices=INTENSITY, blank=True)

    def __str__(self):
        return f"Post {self.id} by {self.user.username}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id} on Post {self.post.id} by {self.user.username}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["post", "user"], name="unique_like_per_user_per_post")
        ]

    def __str__(self):
        return f"{self.user.username} likes Post {self.post.id}"
