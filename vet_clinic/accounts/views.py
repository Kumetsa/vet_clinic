import random
import string

from django.contrib.auth import views as auth_views, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django import forms

from vet_clinic.accounts.forms import VetClinicUserCreationForm
from vet_clinic.accounts.models import Profile, VetClinicUser


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'


class CreateUserView(views.CreateView):
    form_class = VetClinicUserCreationForm
    template_name = 'accounts/create_user.html'

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        # we call login to log the user
        login(self.request, form.instance)

        return result


def logout_user(request):
    logout(request)
    return redirect('index')


class ProfileEditView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'accounts/edit_profile.html'
    fields = ('first_name', 'last_name', 'date_of_birth', 'profile_picture',)

    def get_success_url(self):
        return reverse('details_profile', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date'})

        return form


class ProfileDeleteView(views.DeleteView):
    queryset = VetClinicUser.objects.all()
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = self.get_object()

        # Modify the user's email to append the random string and #deactivated#
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        user.email += f'#deactivated#{random_string}'

        # Set the user to inactive instead of deleting and logout the user
        user.is_active = False
        user.save()
        logout(self.request)

        return HttpResponseRedirect(self.get_success_url())


class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/details_profile.html'

    def get_queryset(self):
        queryset = Profile.objects.prefetch_related('user').all()
        return queryset
