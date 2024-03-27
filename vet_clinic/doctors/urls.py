from django.urls import path

from vet_clinic.doctors.views import MyPatientsListView, PetPatientDetailView, AssignTreatmentView, \
    UnscheduledAppointmentsView, AcceptAppointmentView, DeclineAppointmentView, MyAppointmentsView

urlpatterns = [
    path('my_patients/', MyPatientsListView.as_view(), name='my_patients_list'),
    path('pet_patient/<int:pk>/', PetPatientDetailView.as_view(), name='pet_patient_detail'),
    path('assign_treatment/<int:pk>/', AssignTreatmentView.as_view(), name='assign_treatment'),
    path('unscheduled_appointments/', UnscheduledAppointmentsView.as_view(), name='unscheduled_appointments'),
    path('accept_appointment/<int:pk>/', AcceptAppointmentView.as_view(), name='accept_appointment'),
    path('decline_appointment/<int:pk>/', DeclineAppointmentView.as_view(), name='decline_appointment'),
    path('my_appointments/', MyAppointmentsView.as_view(), name='my_appointments'),

]