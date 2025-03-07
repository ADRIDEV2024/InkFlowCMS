from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'categories', 'tags', 'is_published']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
