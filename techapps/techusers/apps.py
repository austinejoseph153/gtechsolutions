from django.apps import AppConfig


class TechusersConfig(AppConfig):
    name = 'techapps.techusers'
    verbose_name = 'techusers'


    def ready(self):
        import techapps.techusers.signals
