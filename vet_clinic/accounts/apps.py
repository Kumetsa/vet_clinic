from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vet_clinic.accounts'

    def ready(self):
        import vet_clinic.accounts.signals
