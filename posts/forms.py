from django import forms
from .models import Post,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'status']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Post Title'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Write your content here...'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-textarea', 
                'placeholder': 'Write your comment here...'
            })
        }



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']