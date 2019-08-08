from django import forms
from .models import Post, Comment, Like
# bounding form to post model
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('body',)
        labels = {
        "body": ""
        }
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': "What's on your mind?"})
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            "body": ""
        }
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Write a comment...'})
        }
