
from django import forms
from tinymce.widgets import TinyMCE
from .models import Post , Category

  
  
class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        exclude = ('auther',)
        text_input_class = 'outline-none border-2 border-green-200 focus:border-green-300 p-1 '
        widgets = {
            'title':forms.TextInput(attrs={'class':text_input_class}),
            'category':forms.Select(attrs={'class':text_input_class})
        }
  
  
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        text_input_class = 'outline-none border-2 border-green-200 focus:border-green-300 p-1 '
        labels = {
            'cat_name' : "Category Title" ,
            'cat_descr' : "Category Description"
        }
        widgets = {
            'cat_name':forms.TextInput(attrs={'class':text_input_class}),
            'cat_descr':forms.Textarea(attrs={'class':text_input_class})
        }
