from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        
    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['category'].empty_label="Choose Category"
        self.fields['description'].rows = 3
        self.fields['views'].required = False
        self.fields['likes'].required = False