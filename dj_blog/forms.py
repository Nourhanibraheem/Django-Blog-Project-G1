from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UsernameField
from django.core.exceptions import ValidationError

# register form based on built-in usercreationform
class RegistrationForm(UserCreationForm):
    email =  forms.EmailField(required=True,max_length=100)
    class Meta:
        model = User
        fields =['username','email','password1','password2']
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        email =cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exist !")

        # login form inherits from built-in authenticationform 
class LoginForm(AuthenticationForm): 
    username = UsernameField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username..'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password...'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','picture','content','category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'content':forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
        }

class TagsForm(forms.ModelForm):
    class Meta:
        model = PostTags
        fields = ['tag_name']
        widgets = {
            'tag_name': forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tagsinput'})
        }
