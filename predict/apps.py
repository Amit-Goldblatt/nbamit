from django.apps import AppConfig


class PredictConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predict'
    def ready(self):
        from clock import update_season
        update_season()