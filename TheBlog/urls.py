from django.urls import path,include
from django.contrib.auth import views as auth_views
from members.views import PasswordChangeView,PasswordSuccessView
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikePostView,AddCommentView
urlpatterns = [
    # path('',views.home,name="Home")
    path('',HomeView.as_view(),name="Home"),
    # path('<int:pk>/password/',auth_views.PasswordChangeView.as_view(template_name='registration/changePassword.html'),name="ChnagePassword"),
    path('<int:pk>/password/',PasswordChangeView.as_view(template_name='registration/changePassword.html'),name="ChnagePassword"),    
    path('passwordSucess/',PasswordSuccessView,name="passwordSuccess"),
    # articles url
    path('article/<int:pk>',ArticleDetailView.as_view(),name="ArticleDetail"),
    path('addPost/',AddPostView.as_view(),name="AddPost"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='EditPost'),
    path('article/delete/<int:pk>',DeletePostView.as_view(),name="DeletePost"),

    # category url
    path('addCategory/',AddCategoryView.as_view(),name='AddCategory'),
    path('categories/',CategoryListView,name='CategoryList'),
    path('category/<str:cats>/',CategoryView,name='Categories'),
    
    # like/unlike post
    path('likes/<int:pk>',LikePostView,name='likePost'),

    # comments
    path('article/<int:pk>/comment/',AddCommentView.as_view(),name="AddComment"),
]
