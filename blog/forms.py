from django import forms

from .models import Person, Blog

class PersonSignUpForm(forms.ModelForm):
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={
            "id":"username",
        }
    ))
    email = forms.EmailField(label="Email*", widget=forms.EmailInput(
        attrs={
            "id":"email",
        }))
    password = forms.CharField(label="Password*",widget=forms.TextInput(
        attrs={
            "id":"password",
        }
    ))
    confirm_password = forms.CharField(label="Confirm Password*",widget=forms.TextInput(
        attrs={
            "id":"confirm-password",
        }
    ))


    class Meta:
        model = Person
        fields = [
            'username',
            'email',
            'password'
        ]

class PersonLoginForm(forms.ModelForm):
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={
            "id":"username",
            "name":"login-username"
        }
    ))
    password = forms.CharField(label="Password*",widget=forms.PasswordInput(
        attrs={
            "id":"password",
            "name":"login-password"
        }
    ))


    class Meta:
        model = Person
        exclude = ('email', 'profile_img',)


class NewBlogPost(forms.ModelForm):
    title = forms.CharField(label='Title*', widget=forms.TextInput(
        attrs={
            "id":"blog-title",
            "name":"blog-title",
            'size':'40'
        }
    ))

    content = forms.CharField(label='Content*', widget=forms.Textarea(
        attrs={
            "id":"blog-content",
            "name":"blog-content",
            # 'width':'200%',
            'cols':'80',
        }
    ))

    class Meta:
        model = Blog
        exclude = ('date', 'blogger',)