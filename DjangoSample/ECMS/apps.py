from django.apps import AppConfig


class EcmsConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ECMS'

    def ready(self):

        from .scheduler import start
        start()