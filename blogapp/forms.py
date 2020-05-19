from django import forms
from django.contrib.auth.models import User
from blogapp.models import Upload

class UserSignUp(forms.ModelForm):
    class Meta:
        model= User
        #fields='__all__'
        #print(dir(User))
        fields = ['first_name', 'last_name','username', 'password', 'email']
        #widget = {'fieldname': forms.fieldtype(attrs = {'rows':25,'cols': 20})}
        widgets = {'password': forms.PasswordInput()}

class UploadBlog(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['name', 'image', 'description']
