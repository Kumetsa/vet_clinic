from django.shortcuts import render
from django.views import generic as veiws

from vet_clinic.pet_patients.models import PetPatient


class IndexView(veiws.TemplateView):
    template_name = 'web/index.html'
