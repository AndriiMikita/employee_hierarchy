from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from employees.forms import LoginUserForm, RegisterUserForm
from .models import Employee
from .filters import EmployeeFilter
from .utils import build_hierarchy_data, DataMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.template.loader import render_to_string
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView

class EmployeeHierarchyView(View):
    template_name = 'employee_hierarchy.html'

    def get(self, request):
        hierarchy_data = build_hierarchy_data()
        context = {'hierarchy_data': hierarchy_data,
                   'employees' : Employee.objects.all()}
        return render(request, self.template_name, context)

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee.html'
    context_object_name = 'employee'
    
class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employee_list.html'
    paginate_by = 10  # Якщо вам потрібна пагінація

    def get_queryset(self):
        queryset = Employee.objects.all()
        employee_filter = EmployeeFilter(self.request.GET, queryset=queryset)
        return employee_filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EmployeeFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
class RegisterUser(CreateView, DataMixin):
    form_class = RegisterUserForm
    template_name = "register.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('employee-list')
        
class LoginUser(LoginView, DataMixin):
    form_class = LoginUserForm
    template_name = "login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated
        context['user'] = self.request.user
        return context
    
    def get_success_url(self):
        return reverse_lazy('employee-list')
    
def logout_user(request):
    logout(request)
    return redirect('employee-hierarchy')

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = ['full_name', 'position', 'hire_date', 'email', 'head']
    success_url = reverse_lazy('employee-list')
    
class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = ['full_name', 'position', 'hire_date', 'email', 'head']
    success_url = reverse_lazy('employee-list')
    
class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee-list')