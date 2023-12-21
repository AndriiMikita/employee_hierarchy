from django import forms
from django_filters import FilterSet, CharFilter, DateFilter, OrderingFilter
from .models import Employee

class EmployeeFilter(FilterSet):
    full_name = CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )
    position = CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Position'})
    )
    email = CharFilter(
        lookup_expr='icontains',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    hire_date = DateFilter(
        widget=forms.DateInput(attrs={'placeholder': 'Hire Date'}),
        lookup_expr='exact'
    )
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

