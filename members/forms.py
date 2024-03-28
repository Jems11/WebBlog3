from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from TheBlog.models import Profile

class CreateProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','website_url','twitter_url','instagram_url','linkedin_url','facebook_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control my-1'}),
            # 'profile_pic': forms.ImageField(),
            'website_url': forms.TextInput(attrs={'class':'form-control my-1'}),
            'twitter_url': forms.TextInput(attrs={'class':'form-control my-1'}),
            'instagram_url': forms.TextInput(attrs={'class':'form-control my-1'}),
            'linkedin_url': forms.TextInput(attrs={'class':'form-control my-1'}),
            'facebook_url': forms.TextInput(attrs={'class':'form-control my-1'}),
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control my-1'}))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control my-1'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control my-1'}))
    gender = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control my-1'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','gender','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control my-2'
        self.fields['password1'].widget.attrs['class'] = 'form-control my-2'
        self.fields['password2'].widget.attrs['class'] = 'form-control my-2'

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control my-1'}))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control my-1'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control my-1'}))
    username = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control my-1'}))
    # last_login = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control my-1'}))
    # is_superuser = forms.CharField(max_length=200,widget=forms.CheckboxInput(attrs={'class':'form-check my-1'}))
    # is_staff = forms.CharField(max_length=200,widget=forms.CheckboxInput(attrs={'class':'form-check my-1'}))
    # is_active = forms.CharField(max_length=200,widget=forms.CheckboxInput(attrs={'class':'form-check my-1'}))
    # date_joined = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control my-1'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        exclude = ('password',)


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control my-1','type':'password'}))
    new_password1 = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control my-1','type':'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-1','type':'password'}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')
