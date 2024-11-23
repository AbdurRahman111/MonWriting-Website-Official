from django.apps import AppConfig
from googleTrendsApp import job_scheduler

class GoogletrendsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'googleTrendsApp'

    def ready(self) -> None:
        job_scheduler.start()

    # def ready(self):
    #     job_scheduler.start()
        