from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "caption", "workout", "intensity"]
        widgets = {
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "caption": forms.Textarea(attrs={"class": "form-control"}),
            "workout": forms.Select(attrs={"class": "form-select"}),
            "intensity": forms.Select(attrs={"class": "form-select"}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]