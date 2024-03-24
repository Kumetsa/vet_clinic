from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic as views

from vet_clinic.doctors.forms import AssignTreatmentForm
from vet_clinic.pet_patients.models import PetPatient, Treatment


class MyPatientsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = PetPatient
    template_name = 'doctors/my_patients_list.html'
    context_object_name = 'patients'

    def get_queryset(self):
        return PetPatient.objects.filter(doctor=self.request.user)


class PetPatientDetailView(auth_mixins.LoginRequiredMixin, views.View):
    template_name = 'doctors/pet_patient_detail.html'

    def get(self, request, pk):
        pet_patient = get_object_or_404(PetPatient, pk=pk)
        treatments = Treatment.objects.filter(patient=pet_patient)
        return render(request, self.template_name, {'pet_patient': pet_patient, 'treatments': treatments})


class AssignTreatmentView(auth_mixins.LoginRequiredMixin, views.FormView):
    template_name = 'doctors/assign_treatment.html'
    form_class = AssignTreatmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['pet_patient'] = get_object_or_404(PetPatient, pk=pk)
        return context

    def form_valid(self, form):
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(PetPatient, pk=patient_id)
        treatment_data = form.cleaned_data
        treatment_data['patient'] = patient
        treatment_data['doctor'] = self.request.user
        Treatment.objects.create(**treatment_data)
        return redirect('pet_patient_detail', pk=patient_id)

