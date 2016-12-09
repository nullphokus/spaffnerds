from django.apps import AppConfig


class SetlistsConfig(AppConfig):
    name = 'spaffnerds.setlists'
    verbose_name = "Setlists"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
