from django import forms

from .models import Comment, Post, Category


class AddPostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'photo', 'category', 'author')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'author', 'type': 'hidden'}),
            'category': forms.Select(choices=Category.objects.all(), attrs={'class': 'form-control'}),
        }

class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type your comment'})
        }

