from django import forms
from .models import ThreadModel, PostModel


class ThreadModelForm(forms.ModelForm):

    class Meta:
        model = ThreadModel
        fields = ['text', 'image']


class PostModelForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ['text', 'image']

