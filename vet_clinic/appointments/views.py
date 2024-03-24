from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from vet_clinic.appointments.forms import AppointmentForm
from vet_clinic.appointments.models import Appointment


class AppointmentCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/create_appointment.html'
    success_url = reverse_lazy('user_appointment_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs

    def get_success_url(self):
        return reverse('user_appointment_list', kwargs={'pk': self.request.user.pk})


class AppointmentListView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'appointments/user_appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        # Filter appointments by the currently logged-in user
        return Appointment.objects.filter(created_by=self.request.user)


class AppointmentDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Appointment
    template_name = 'appointments/detail_appointment.html'

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        appointment = self.get_object()
        context['appointment'] = appointment
        return context


class AppointmentEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/edit_appointment.html'
    success_url = reverse_lazy('user_appointment_list')

    def get_success_url(self):
        return reverse('user_appointment_list', kwargs={'pk': self.request.user.pk})

    def get_queryset(self):
        return Appointment.objects.filter(created_by=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs


class AppointmentDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Appointment
    success_url = reverse_lazy('user_appointment_list')

    def get_success_url(self):
        return reverse('user_appointment_list', kwargs={'pk': self.request.user.pk})

    def get_queryset(self):
        return Appointment.objects.filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
