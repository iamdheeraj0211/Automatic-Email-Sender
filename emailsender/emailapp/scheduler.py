from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from emailapp.tasks import send_event_emails


def schedule_task():
    # Create a scheduler
    scheduler = BackgroundScheduler()

    # Schedule the task to run at a specific time (e.g., 9:05 PM India time)
    scheduler.add_job(send_event_emails, 'cron', hour=23, minute=39)

    # Start the scheduler
    scheduler.start()
