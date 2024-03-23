from django.contrib.auth import views as auth_views, login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from vet_clinic.accounts.forms import VetClinicUserCreationForm


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'


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
