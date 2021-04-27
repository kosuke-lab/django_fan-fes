from django import forms
from . import models
from .models import Comment
from .models import Festival


class ContactForm(forms.Form):
   name = forms.CharField(label='お名前', max_length=50)
   email = forms.EmailField(label='メールアドレス',)
   message = forms.CharField(label='メッセージ', widget=forms.Textarea)

class  PostForm(forms.ModelForm):
    class Meta :
        model =Festival
        fields = ('name', 'area', 'country', 'location', 'start_time', 'thumbnail', 'detail' ,'author') 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text','author') 
        widgets = {
            'text': forms.Textarea(attrs={'rows':7, 'cols':100}),
            'author' :forms.Textarea(attrs={'rows':1, 'cols':30}),
        }   



