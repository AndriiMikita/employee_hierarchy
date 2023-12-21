from django_filters import FilterSet, CharFilter, DateFilter, OrderingFilter
from .models import Employee

class EmployeeFilter(FilterSet):
    full_name = CharFilter(lookup_expr='icontains')
    position = CharFilter(lookup_expr='icontains')
    email = CharFilter(lookup_expr='icontains')
    hire_date = DateFilter()
    order_by = OrderingFilter(
        fields=('full_name', 'position', 'email', 'hire_date',),
        field_labels={'hire_date': 'Experience',
                      'full_name': 'Full Name',
                      'position': 'Position',
                      'email': 'Email',},
    )

    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'email', 'hire_date']
