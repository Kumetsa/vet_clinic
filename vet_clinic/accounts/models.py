from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

from vet_clinic.accounts.managers import VetClinicUserManager


class VetClinicUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    is_doctor = models.BooleanField(
        _("doctor status"),
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = VetClinicUserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_doctor:
            doctor_group, _ = Group.objects.get_or_create(name='Doctors')
            self.groups.add(doctor_group)


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30
    MAX_LENGTH_PHONE = 25

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # TODO: make this image field to upload the picture.
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    phone = models.CharField(
        max_length=MAX_LENGTH_PHONE,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        VetClinicUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        if self.first_name and self.first_name:
            return f"{self.first_name} {self.last_name}"

        return self.first_name or self.last_name
