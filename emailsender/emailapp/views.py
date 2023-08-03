from .models import Employee, EmployeeEvent, EmailTemplate
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.shortcuts import render
from datetime import date


class Command(BaseCommand):
    help = 'Send personalized emails for employee events'

    def handle(self, *args, **kwargs):
        today = date.today()

        employees_with_event = EmployeeEvent.objects.filter(
            event_date__month=today.month, event_date__day=today.day)

        for event in employees_with_event:
            employee = event.employee
            event_type = event.event_type
            email_template = EmailTemplate.objects.get(event_type=event_type)
            email_subject = email_template.subject.replace(
                '{employee_name}', employee.name)
            email_content = email_template.subject.replace(
                '{employee_name}', employee.name)

            try:
                send_mail(
                    subject=email_subject,
                    message=email_content,
                    from_email='iamdheeraj0211@.com',
                    recipient_list=[employee.email],
                    fail_silently=False,
                )
                # Log the email sending status
                self.stdout.write(self.style.SUCCESS(
                    f'Successfully sent email to {employee.name}'))
            except Exception as e:
                # Log any errors encountered during email sending
                self.stdout.write(self.style.ERROR(
                    f'Error sending email to {employee.name}: {str(e)}'))
