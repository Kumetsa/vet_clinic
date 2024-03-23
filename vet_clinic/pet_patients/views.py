from django.urls import reverse_lazy, reverse
from django.views import generic as views

from vet_clinic.pet_patients.forms import PetPatientCreateForm
from vet_clinic.pet_patients.models import PetPatient
from django.contrib.auth import mixins as auth_mixins


# TODO: update
class PetDetailView(views.DetailView):
    # template_name = 'pet_patients/detail_pet_patient.html'
    # context_object_name = 'pet'
    pass


class PetCreateView(views.CreateView, auth_mixins.LoginRequiredMixin):
    form_class = PetPatientCreateForm
    template_name = 'pet_patients/create_pet_patient.html'
    success_url = reverse_lazy('my_pets')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form

    def get_success_url(self):
        user_pk = self.request.user.pk
        return reverse_lazy('my_pets', kwargs={'pk': user_pk})


# TODO: update
class PetEditView(views.UpdateView):
    model = PetPatient
    fields = ['name', 'species', 'breed', 'date_of_birth', 'weight', 'gender', 'color', 'notes']
    template_name = 'pet_patients/edit_pet_patient.html'
    success_url = 'index'


# TODO: update
class PetDeleteView(views.DeleteView):
    model = PetPatient
    template_name = 'pet_patients/delete_pet_patient.html'
    success_url = reverse_lazy('index')


class MyPetsView(views.ListView):
    template_name = 'pet_patients/my_pets.html'
    context_object_name = 'pets'

    def get_queryset(self):
        return PetPatient.objects.filter(user=self.request.user)
