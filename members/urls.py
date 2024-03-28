from django.urls import path,include
from .views import UserRegisterView,UserEditView,ShowProfilePageView,EditProfilePageView,CreateProfilePageView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name="Register"),
    path('editProfile/',UserEditView.as_view(),name="EditProfile"),
    
    path('<int:pk>/profile/',ShowProfilePageView.as_view(),name="ShowProfile"),
    
    path('createProfilePage/',CreateProfilePageView.as_view(),name="CreateProfilePage"),
    path('<int:pk>/editProfile/',EditProfilePageView.as_view(),name="EditProfilePage"),
]
