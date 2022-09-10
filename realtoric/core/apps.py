from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "realtoric.core"

    def ready(self):
        try:
            import realtoric.core.signals  # noqa F401
        except ImportError:
            pass
