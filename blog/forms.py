
from django import forms
from blog.models import Blog


#blog form
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields= ["title","content","image"]