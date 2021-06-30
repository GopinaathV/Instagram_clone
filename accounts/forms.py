from django import forms
from post.models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"

class ProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "location", "profile_info", "picture", "phone_no", "gender")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EditProfileForm(forms.ModelForm):

    username = forms.CharField(required=True)
    location = forms.CharField(required=True)
    profile_info = forms.CharField(required=True)
    picture= forms.ImageField(required=True)
    phone_no = forms.CharField(required=True)
    email = forms.CharField( required=True)
    gender= models.CharField(choices=GENDER_CHOICES,max_length=10,default='M')


    class Meta:
        model = Profile
        fields = ('username','location','profile_info','picture', 'phone_no', 'email','gender')


class NewPostForm(forms.ModelForm):
	picture = forms.ImageField(required=True)
	caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
	tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)

	class Meta:
		model = Post
		fields = ('picture', 'caption', 'tags')
