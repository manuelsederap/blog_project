from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    """Create a Post form from a Model"""

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        # connect form into css using widgets
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):
    """Create a Comment form from a Model"""

    class Meta():
        model = Comment
        fields = ('author', 'text')

        # connect form into css using widgets
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
