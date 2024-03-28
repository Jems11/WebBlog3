from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile")
    website_url = models.CharField(max_length=250,null=True,blank=True)
    twitter_url = models.CharField(max_length=250,null=True,blank=True)
    instagram_url = models.CharField(max_length=250,null=True,blank=True)
    linkedin_url = models.CharField(max_length=250,null=True,blank=True)
    facebook_url = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.user.first_name)
    
    def get_absolute_url(self):
        return reverse('Home')

class Category(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.category

    def get_absolute_url(self):
        return reverse('Home')
    
class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=255,default="This is tech blog")
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255,default="Uncategorized")
    snippets = models.CharField(max_length=255,default="Click Above link to show post..")
    likes = models.ManyToManyField(User,related_name='blog_post')
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # so below method is use for redirect to detail page of new created blog
        # return reverse('ArticleDetail',args=(str(self.id)))
        # and below method is used for redirect to home page.
        return reverse('Home')
    
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.post.title + ' - ' + self.name     
    
