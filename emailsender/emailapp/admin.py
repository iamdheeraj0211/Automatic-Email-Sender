from django.contrib import admin
from .models import Employee, EmployeeEvent, EmailTemplate, EmailLog
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        model = Employee
        list_display = '__all__'


@admin.register(EmployeeEvent)
class EmployeeEventAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeEvent
        list_display = "__all__"


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    class Meta:
        model = EmailTemplate
        list_display = "__all__"


@admin.register(EmailLog)
class EmaillogAdmin(admin.ModelAdmin):
    class Meta:
        model = EmailLog
        list_display = "__all__"
