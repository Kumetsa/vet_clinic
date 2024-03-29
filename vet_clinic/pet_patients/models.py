from django.db import models
from django.contrib.auth import get_user_model

from vet_clinic.pet_patients.validators import validate_positive_weight

UserModel = get_user_model()


class PetPatient(models.Model):
    MAX_LENGTH_PATIENT_NAME = 50
    MAX_LENGTH_SPECIES_NAME = 25
    MAX_LENGTH_BREED_NAME = 100

    DOG = 'Dog'
    CAT = 'Cat'
    BIRD = 'Bird'
    RABBIT = 'Rabbit'
    HAMSTER = 'Hamster'
    FISH = 'Fish'
    TURTLE = 'Turtle'
    GUINEA_PIG = 'Guinea Pig'
    SNAKE = 'Snake'
    HORSE = 'Horse'
    OTHER = 'Other'

    SPECIES_CHOICES = [
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (BIRD, 'Bird'),
        (RABBIT, 'Rabbit'),
        (HAMSTER, 'Hamster'),
        (FISH, 'Fish'),
        (TURTLE, 'Turtle'),
        (GUINEA_PIG, 'Guinea Pig'),
        (SNAKE, 'Snake'),
        (HORSE, 'Horse'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(
        max_length=MAX_LENGTH_PATIENT_NAME,
    )

    species = models.CharField(
        max_length=MAX_LENGTH_SPECIES_NAME,
        choices=SPECIES_CHOICES,
    )

    breed = models.CharField(
        max_length=MAX_LENGTH_BREED_NAME,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField()

    weight = models.FloatField(
        validators=[validate_positive_weight],
    )

    gender = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
        ],
    )

    color = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='pets',
    )

    doctor = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Treatment(models.Model):
    MAX_LENGTH_DIAGNOSE_TYPE = 50
    MAX_LENGTH_TREATMENT_TYPE = 100

    patient = models.ForeignKey(
        PetPatient,
        on_delete=models.CASCADE,
    )

    doctor = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    date = models.DateField()

    diagnose = models.CharField(
        max_length=MAX_LENGTH_DIAGNOSE_TYPE,
    )

    treatment_type = models.CharField(
        max_length=MAX_LENGTH_TREATMENT_TYPE,
    )

    description = models.TextField()

    def __str__(self):
        return f"Treatment for {self.patient.name} on {self.date}"

