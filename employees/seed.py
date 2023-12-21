from django_seed import Seed
from employees.models import Employee
import datetime

seeder = Seed.seeder()    

    
def create_employees(total):
    for _ in range(total):
        full_name = seeder.faker.name()
        hire_date = seeder.faker.date_between_dates(date_start=datetime.date(2015, 1, 1), date_end=datetime.date.today())
        email = f"{full_name.replace(' ', '.').lower()}@example.com"
        head = seeder.faker.random_element(Employee.objects.all()) if Employee.objects.exists() else None
        position = 0 if head is None else int(head.position) + 1
        employee = {
            'full_name': full_name,
            'position': position,
            'hire_date': hire_date,
            'email': email,
            'head': head,
        }
    
        seeder.add_entity(Employee, 1, employee)
    
        seeder.execute()
