from django import forms
from blog.models import Post,Comment
from django.db.models import Q

class HomeForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(          #gives bootstrap class

    attrs={
              'class': 'form-control',
              'placeholder':'Enter Title'

        }
        ))
    post=forms.CharField(widget=forms.Textarea(          #gives bootstrap class

    attrs={
          'class': 'form-control',
          'placeholder':'Write a post'

    }
    ))

    class Meta:
        model = Post
        fields = ('title','post',)
class CommentForm(forms.ModelForm):

    text=forms.CharField(widget=forms.Textarea(          #gives bootstrap class

    attrs={
          'class': 'form-control',
          'placeholder':'Write a post'

    }
    ))

    class Meta:
        model = Comment
        fields = ('author','text',)
    def __init__(self, user, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        
