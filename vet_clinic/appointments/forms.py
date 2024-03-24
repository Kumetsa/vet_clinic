from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

from vet_clinic.appointments.models import Appointment
from vet_clinic.pet_patients.models import PetPatient

UserModel = get_user_model()


class AppointmentForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=PetPatient.objects.none(), empty_label="Select Pet")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.Select(choices=[]))

    class Meta:
        model = Appointment
        fields = ['date', 'time', 'purpose', 'patient']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = PetPatient.objects.filter(user=user)


        # Choices for date field
        today = datetime.now().date()
        end_date = today + timedelta(days=30)
        self.fields['date'].widget.attrs['min'] = today
        self.fields['date'].widget.attrs['max'] = end_date

        # Choices for time field
        time_choices = [(datetime.min + timedelta(minutes=i)).time().strftime('%H:%M') for i in range(0, 24*60, 30)]
        self.fields['time'].widget.choices = [(choice, choice) for choice in time_choices]

        for field_name, field in self.fields.items():
            if field_name != 'doctor':
                field.required = True

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            selected_datetime = datetime.combine(date, time)
            if selected_datetime <= datetime.now():
                raise ValidationError("Selected date and time must be in the future.")

        return cleaned_data

    def save(self, commit=True):
        appointment = super().save(commit=False)
        appointment.date_time = datetime.combine(self.cleaned_data['date'], self.cleaned_data['time'])
        if commit:
            appointment.save()
        return appointment
