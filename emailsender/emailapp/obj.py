from emailapp.models import Employee, EmployeeEvent
# employee = Employee.objects.create(
#     name='John Doe',
#     email='john.doe@example.com',
#     dob='1990-08-03',
#     doj='2022-08-03', )

employee = Employee.objects.get(id=1)
event = EmployeeEvent.objects.create(
    employee=employee, event_type="Birthday", event_date=employee.dob)
event2 = EmployeeEvent.objects.create(
    employee=employee, event_type="Work Anniversary", event_date=employee.doj)
with open('emailapp/views.py') as file:
    code = compile(file.read(), 'emailapp/views.py', 'exec')
    exec(code)
