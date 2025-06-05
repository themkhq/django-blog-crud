from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full p-2 border rounded",
                    "placeholder": "Write Blog Title...",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "w-full p-2 border rounded",
                    "rows": 5,
                }
            ),
        }