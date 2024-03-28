from django import forms
from .models import Post,Category,Comment

# hard coded choices
# choices = [('coding1','coding'),('programming','programming')]
# populate all choices from db
choices = Category.objects.all().values_list('category','category').order_by('category')
choices_list = [choice for choice in choices]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippets','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Please enter blog title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control my-1'}),
            'author': forms.TextInput(attrs={'class':'form-control my-1','placeholder':'username','id':'authorName','value':'','type':'hidden'}),
            # 'author': forms.Select(attrs={'class':'form-control my-1'}),
            'category': forms.Select(choices=choices_list,attrs={'class':'form-control my-1'}),
            'body': forms.Textarea(attrs={'class':'form-control my-1','placeholder':'Start wrting your blog here..'}),
            'snippets': forms.Textarea(attrs={'class':'form-control my-1','placeholder':'Enter snippets'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','snippets')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-1','placeholder':'blog title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control my-1'}),
            'category': forms.Select(choices=choices_list,attrs={'class':'form-control my-1'}),
            # 'author': forms.Select(attrs={'class':'form-control my-1'}),
            'body': forms.Textarea(attrs={'class':'form-control my-1','placeholder':'Start wrting your blog here..'}),
            'snippets': forms.Textarea(attrs={'class':'form-control my-1','placeholder':'Enter snippets'})

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control my-1'}),
            'body': forms.Textarea(attrs={'class':'form-control my-1','placeholder':'Write Your Comment'}),
        }
