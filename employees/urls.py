from django.urls import path
from .views import EmployeeHierarchyView, EmployeeDetailView, EmployeeListView, RegisterUser, LoginUser, logout_user, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('hierarchy/', EmployeeHierarchyView.as_view(), name='employee-hierarchy'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('list/', EmployeeListView.as_view(), name='employee-list'),
    path('', EmployeeListView.as_view(), name='employee-list-home'),
    path('register/', RegisterUser.as_view(), name="register"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('add/', EmployeeCreateView.as_view(), name="employee-add"),
    path('edit/<int:pk>', EmployeeUpdateView.as_view(), name="employee-edit"),
    path('delete/<int:pk>/', EmployeeDeleteView.as_view(), name="employee-delete"),
]