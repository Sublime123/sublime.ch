from django import forms

from .models import Post
from .models import Threads

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'msg', 'img')
        widgets = {
            'msg': forms.Textarea(),
        }

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Post
        models = (Threads,Post)
        fields = ('title', 'msg', 'img')
        widgets = {
            'msg': forms.Textarea(),
        }