from django import forms
from .models import BlogEntry

class BlogForm(forms.ModelForm):
    title = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(('slug'), max_length=50, unique=True, populate_from=('title',))
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    category = models.ForeignKey('BlogEntry.BlogCategory.title', on_delete=models.CASCADE)
    Images = None
    CodeSnippets = None

    class Meta:
        model = Post
        fields = ("title", "body", "Images", "CodeSnippets", "posted", "category", "user", "slug")


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    

    class Meta:
        model = Images
        fields = ('image', ) 

class CodeSnippetForm(forms.ModelForm):
    CodeSnippet = forms.CharField(label='Code snippet')
    
    class Mate:
        model = CodeSnippets
        fields = ('code', )
