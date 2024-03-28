from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from .forms import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-post_date']
    paginate_by = 5
    
    def get_context_data(self,*args,**kwargs):
        cats_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cats_menu"] = cats_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articleDetail.html'

    def get_context_data(self,*args,**kwargs):
        cats_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        post_details = get_object_or_404(Post,id=self.kwargs['pk'])
        related_post = Post.objects.filter(author=post_details.author.id)
        total_likes = post_details.total_likes()

        liked = False
        if post_details.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cats_menu"] = cats_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        context['related_post'] = related_post
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addPost.html'
    # below method used for getting all form fields
    # fields = '__all__'
    # below method is used for getting selected fields
    # fields = ('title','body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatePost.html'
    # fields = ['title','title_tag','body']
    success_url = reverse_lazy('Home')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('Home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'addCategory.html'
    fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'addComments.html'
    # fields = '__all__'
    success_url = reverse_lazy('Home')

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

def CategoryView(request,cats):
    category_blog_post = Post.objects.filter(category=cats.replace('-',' '))
    return render(request=request,template_name='category.html',context={'cats':cats.replace('-',' '),'category_Post':category_blog_post})

def CategoryListView(request):
    cats_menu_list = Category.objects.all()
    return render(request=request,template_name='categoryList.html',context={'cats_menu_list':cats_menu_list})

def LikePostView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('like_post_id'))

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse_lazy('ArticleDetail',args=[str(pk)]))