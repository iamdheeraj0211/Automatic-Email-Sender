from django.apps import AppConfig


class EmailappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emailapp'

    def ready(self):
        # Schedule the task when the app is ready
        from .scheduler import schedule_task
        schedule_task()
