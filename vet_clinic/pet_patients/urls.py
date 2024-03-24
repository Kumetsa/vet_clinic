from django.urls import path
from vet_clinic.pet_patients.views import PetCreateView, PetDeleteView, PetDetailView, PetEditView

urlpatterns = [
    path('create/', PetCreateView.as_view(), name='create_pet_patient'),
    path('<int:pk>/', PetDetailView.as_view(), name='detail_pet_patient'),
    path('<int:pk>/edit/', PetEditView.as_view(), name='edit_pet_patient'),
    path('<int:pk>/delete/', PetDeleteView.as_view(), name='delete_pet_patient'),
]
