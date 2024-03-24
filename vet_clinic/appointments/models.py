from django.contrib.auth import get_user_model
from django.db import models

from vet_clinic.pet_patients.models import PetPatient

UserModel = get_user_model()


class Appointment(models.Model):
    MAX_LENGTH_PURPOSE = 255

    date_time = models.DateTimeField()

    purpose = models.CharField(
        max_length=MAX_LENGTH_PURPOSE,
        blank=True,
    )

    patient = models.ForeignKey(
        PetPatient,
        on_delete=models.CASCADE,
    )

    doctor = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='created_by',
    )

    is_accepted = models.BooleanField()

    def __str__(self):
        doctor_name = self.doctor.full_name if self.doctor else ""
        formatted_date_time = self.date_time.strftime("%Y-%m-%d %H:%M")
        if doctor_name:
            return f"Appointment for {self.patient.name} with Dr. {doctor_name} at {formatted_date_time}"
        else:
            return f"Appointment for {self.patient.name} at {formatted_date_time}"



