from django.urls import path

from vet_clinic.doctors.views import MyPatientsListView, PetPatientDetailView, AssignTreatmentView

urlpatterns = [
    path('my_patients/', MyPatientsListView.as_view(), name='my_patients_list'),
    path('pet_patient/<int:pk>/', PetPatientDetailView.as_view(), name='pet_patient_detail'),
    path('assign_treatment/<int:pk>/', AssignTreatmentView.as_view(), name='assign_treatment'),
]