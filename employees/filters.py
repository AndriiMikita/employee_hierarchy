from django_filters import FilterSet, CharFilter, DateFilter
from .models import Employee

class EmployeeFilter(FilterSet):
    full_name = CharFilter(lookup_expr='icontains')
    position = CharFilter(lookup_expr='icontains')
    email = CharFilter(lookup_expr='icontains')
    hire_date = DateFilter()

    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'email', 'hire_date']
