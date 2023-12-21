from .models import Employee

def build_hierarchy(root_employee):
    hierarchy = {'name': f"{root_employee.full_name} - {root_employee.position}", 'children': [], 'data': {'id' : root_employee.id,
                                                                                                           'full_name': root_employee.full_name,
                                                                                                           'position': root_employee.position,
                                                                                                           'email': root_employee.email}}
    children = Employee.objects.filter(head=root_employee)
    for child in children:
        hierarchy['children'].append(build_hierarchy(child))
    return hierarchy

def build_hierarchy_data():
    root_employee = Employee.objects.get(head=None)
    hierarchy_data = build_hierarchy(root_employee)
    return hierarchy_data

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['authenticated'] = self.request.user.is_authenticated
        return context