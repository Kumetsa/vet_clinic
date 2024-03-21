from django.db import models
from django.contrib.auth import get_user_model

from vet_clinic.pet_patients.validators import validate_positive_weight

UserModel = get_user_model()


class Owner(models.Model):
    MAX_LENGTH_FIRST_NAME = 50
    MAX_LENGTH_LAST_NAME = 50
    MAX_LENGTH_PHONE = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=MAX_LENGTH_PHONE,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Species(models.Model):
    MAX_LENGTH_SPECIES_NAME = 20

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
        max_length=MAX_LENGTH_SPECIES_NAME,
        choices=SPECIES_CHOICES,
        unique=True,
    )

    def __str__(self):
        return self.name


class PetPatient(models.Model):
    MAX_LENGTH_PATIENT_NAME = 50
    MAX_LENGTH_SPECIES_NAME = 100
    MAX_LENGTH_BREED_NAME = 100

    name = models.CharField(
        max_length=MAX_LENGTH_PATIENT_NAME,
    )

    species = models.ForeignKey(
        Species,
        on_delete=models.CASCADE,
    )

    breed = models.CharField(
        max_length=MAX_LENGTH_BREED_NAME,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField()

    owner = models.ForeignKey(
        Owner,
        on_delete=models.RESTRICT,
    )

    doctor = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

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

    def __str__(self):
        return self.name


class Treatment(models.Model):
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

    treatment_type = models.CharField(
        max_length=MAX_LENGTH_TREATMENT_TYPE,
    )

    description = models.TextField()

    def __str__(self):
        return f"Treatment for {self.patient.name} on {self.date}"

    class Appointment(models.Model):
        MAX_LENGTH_PURPOSE = 255

        patient = models.ForeignKey(
            PetPatient,
            on_delete=models.CASCADE,
        )

        doctor = models.ForeignKey(
            UserModel,
            on_delete=models.CASCADE,
        )

        date_time = models.DateTimeField()

        purpose = models.CharField(
            max_length=MAX_LENGTH_PURPOSE,
            blank=True,
        )

        def __str__(self):
            return f"Appointment for {self.patient.name} with Dr. {self.doctor.full_name()} at {self.date_time}"
        