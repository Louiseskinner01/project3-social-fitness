from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "caption", "workout", "intensity"]
        widgets = {
            "image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
            "caption": forms.Textarea(attrs={"class": "form-control"}),
            "workout": forms.Select(attrs={"class": "form-select"}),
            "intensity": forms.Select(attrs={"class": "form-select"}),
        }
## Code below is from ChatGPT to help enusre the user cant submit an empty form
    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get("image")

        if not image:
            raise forms.ValidationError("You must upload an image.")

        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
