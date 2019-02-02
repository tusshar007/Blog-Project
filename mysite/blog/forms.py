from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        #widgets help in connecting forms with the CSS classes
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            # the following value of class are CSS libraries
            # Project classes :textinputclass , postcontent these are user defined for this project

            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    clas Meta():
    model= Comment
    fields=('author','text')

    widgets={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
    }
