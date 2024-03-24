from django.urls import path

from vet_clinic.appointments.views import AppointmentCreateView, AppointmentListView, AppointmentEditView, \
        AppointmentDetailView, AppointmentDeleteView

urlpatterns = [
        path('<int:pk>/appointments/', AppointmentListView.as_view(), name='user_appointment_list'),
        path('<int:pk>/details/', AppointmentDetailView.as_view(), name='details_appointment'),
        path('<int:pk>/create/', AppointmentCreateView.as_view(), name='create_appointment'),
        path('<int:pk>/edit/', AppointmentEditView.as_view(), name='edit_appointment'),
        path('<int:pk>/delete/', AppointmentDeleteView.as_view(), name='delete_appointment'),
]