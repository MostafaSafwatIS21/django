from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'author', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200',
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200',
                'rows': 8,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2 text-sm text-gray-700',
            }),
            'author': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2 focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200',
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'rounded border-gray-300 text-indigo-600 focus:ring-indigo-500',
            }),
        }
