from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm,EditProfileForm,PasswordChangingForm,CreateProfilePageForm
from TheBlog.models import Profile
# Create your views here.

class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = CreateProfilePageForm
    template_name = 'registration/createProfilePage.html'
    # fields = '__all__'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = CreateProfilePageForm
    template_name = 'registration/editProfilePage.html'
    # fields = ['bio','profile_pic','website_url','twitter_url','instagram_url','linkedin_url','facebook_url']    
    success_url = reverse_lazy('Home')   

    # def get_object(self):
    #     return self.request.user 

class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/userProfile.html'

    def get_context_data(self,*args,**kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)

        user_profile = get_object_or_404(Profile,id=self.kwargs['pk'])
        context["user_profile"] = user_profile
        return context
    
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('passwordSuccess')

def PasswordSuccessView(request):
    return render(request,'registration/passwordSuccess.html')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/editProfile.html'
    success_url = reverse_lazy('Home')

    def get_object(self):
        return self.request.user

