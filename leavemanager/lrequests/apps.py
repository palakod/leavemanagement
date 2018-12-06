from django.apps import AppConfig


class LrequestsConfig(AppConfig):
    name = 'lrequests'
    verbose_name = ('L.E.A.V.E.S')

    def ready(self):
        import lrequests.signals