from django import forms
from .models import Post, Comment, Topic


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
    topic = forms.ModelChoiceField(queryset=Topic.objects.all())


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
