from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DeleteView
# from django.contrib.auth.views import TemplateView()
from .forms import SignUpFrom, EditAccountForm, ChangePasswordForm, EditProfileForm, UserResetPasswordForm, UserSetPasswordForm, EditFrom
from web_site.models import Profile, Post
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth.forms import PasswordResetForm




class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = SignUpFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Registration was successfully completed'

class UserEditAccountView(SuccessMessageMixin, UpdateView):
    form_class = EditAccountForm
    template_name = 'registration/change_account.html'
    success_url = reverse_lazy('change_account')
    success_message = 'Account data successfully updated'

    def get_object(self):
        return self.request.user

class UserChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('change_account')
    success_message = 'Password Changed successfully'

class UserShowProfileView(ListView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        print(self.kwargs)
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        post = Post.objects.filter(author=user)

        user_page, created = Profile.objects.get_or_create(user=user)
        context["user_page"] = user_page
        context["user_post"] = post
        return context

class UserEditProfile(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

class UserResetPasswordView(SuccessMessageMixin, PasswordResetView):
    form_class = UserResetPasswordForm
    template_name = 'registration/reset_password.html'
    success_message = 'Check your email!!!'
    success_url = reverse_lazy('login')

class UserSetPasswordView(SuccessMessageMixin, PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    template_name = 'registration/set_password.html'
    success_url = reverse_lazy('login')
    success_message = 'Password reset request completed successfully'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditFrom
    template_name = 'registration/update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'registration/delete.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
 