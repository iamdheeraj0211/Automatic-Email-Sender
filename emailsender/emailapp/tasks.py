from models import Employee, EmployeeEvent, EmailTemplate, EmailLog
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from datetime import date
import logging
import time
from django.conf import settings
# email_system/management/commands/send_event_emails.py
from celery import shared_task


@shared_task
def send_event_emails():
    help = 'Send personalized emails for employee events'
    max_retries = 3

    today = date.today()

    logger = logging.getLogger('django.core.mail')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(levelname)s %(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    file_handler = logging.FileHandler(
        'C:/Users/DHEERAJ/Desktop/Data-Axle/emailsender/emailapp/management/commands/email_log.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    employees_with_event = EmployeeEvent.objects.filter(
        event_date__month=today.month, event_date__day=today.day)

    for event in employees_with_event:
        employee = event.employee
        event_type = event.event_type
        email_template = EmailTemplate.objects.get(event_type=event_type)
        email_subject = email_template.subject.replace(
            '{employee_name}', employee.name)
        email_content = email_template.content.replace(
            '{employee_name}', employee.name)

        no_of_tries = 0
        success = False

        while not success and no_of_tries < settings.MAX_EMAIL_RETRIES:

            try:
                send_mail(
                    subject=email_subject,
                    from_email=settings.EMAIL_HOST_USER,
                    message=email_content,
                    recipient_list=[employee.email],
                    fail_silently=False,
                )
                # Log the email sending status
                logger = logging.getLogger('django.core.mail')
                s = logger.info(
                    f'Successfully sent email to {employee.name} on his {event_type}')
                success = True
                emaillog = EmailLog.objects.create(
                    employee=event.employee, status=f"Successfully sent email to {employee.name} on his {event_type}")

            except Exception as e:
                # Log any errors encountered during email sending
                logger.error(
                    f'Error sending email to {employee.name}: {str(e)} on his {event_type}')
                emaillog = EmailLog.objects.create(
                    employee=event.employee, status=f"Error sending email to {employee.name}: {str(e)} on his {event_type}")

                no_of_tries += 1

                time.sleep(settings.EMAIL_RETRY_DELAY)

        if not success:
            logger.error(
                f'Failed to send email to {employee.name} after {settings.MAX_EMAIL_RETRIES} attempts')
            emaillog = EmailLog.objects.create(
                employee=event.employee, status=f'Failed to send email to {employee.name} after {settings.MAX_EMAIL_RETRIES} attempts')
