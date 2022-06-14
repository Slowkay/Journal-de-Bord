from dataclasses import field
from django import forms

from .models import Folder, Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'folder',)
        

class FolderForm(forms.ModelForm):
    
    class Meta:
        model = Folder
        fields = ('name',)