from django.urls import reverse_lazy, reverse
from django.views import generic as views

from vet_clinic.pet_patients.forms import PetPatientCreateForm, PetPatientEditForm
from vet_clinic.pet_patients.models import PetPatient
from django.contrib.auth import mixins as auth_mixins


class PetDetailView(views.DetailView, auth_mixins.LoginRequiredMixin):
    template_name = 'pet_patients/detail_pet_patient.html'
    context_object_name = 'pet'

    def get_queryset(self):
        return PetPatient.objects.filter(user=self.request.user)


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


class PetEditView(views.UpdateView):
    form_class = PetPatientEditForm
    template_name = 'pet_patients/edit_pet_patient.html'
    success_url = reverse_lazy('my_pets')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['date_of_birth'].widget.attrs.update({'type': 'date'})
        return form

    def get_queryset(self):
        return PetPatient.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('my_pets', kwargs={'pk': self.object.pk})


# TODO: update
class PetDeleteView(views.DeleteView):
    model = PetPatient
    template_name = 'pet_patients/delete_pet_patient.html'
    success_url = reverse_lazy('my_pets')

    def get_queryset(self):
        return PetPatient.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('my_pets', kwargs={'pk': self.object.pk})
