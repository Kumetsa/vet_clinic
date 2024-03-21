from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from vet_clinic.accounts.models import Profile

UserModel = get_user_model()

"""
This function is triggered when a new user is created.
It creates a new Profile object for the user.

Args:
    sender (object): The model class that sent the signal.
    instance (object): The newly created user instance.
    created (bool): A boolean indicating whether the user was created or updated.
    **kwargs (dict): Any additional keyword arguments.

Returns:
    None
"""


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    # created = False, when the user is updated
    # created = True, when the user is created
    if not created:
        return

    Profile.objects.create(user=instance)