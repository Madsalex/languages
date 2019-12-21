from django import forms

from .models import *


class CreateForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'language', 'text', 'tags',)
