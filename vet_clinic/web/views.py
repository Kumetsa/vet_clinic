from django.shortcuts import render
from django.views import generic as views

from vet_clinic.pet_patients.models import PetPatient


class IndexView(views.TemplateView):
    template_name = 'web/index.html'


class MyPetsView(views.ListView):
    template_name = 'web/my_pets.html'
    context_object_name = 'pets'

    def get_queryset(self):
        return PetPatient.objects.filter(user=self.request.user)