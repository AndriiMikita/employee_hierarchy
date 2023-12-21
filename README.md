# Employee Management System

This is a Django project for managing employees.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python (3.9)
- Git

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/employee-management.git
```

2. Navigate to the project directory:
   
```bash
cd employee-management
```

3. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

### Running the Server

1. Run the Django development server:

```bash
python manage.py runserver
```

2. Open your web browser and go to [http://localhost:8000](http://localhost:8000).

### Accessing the Application

The application can be accessed locally at [http://localhost:8000](http://localhost:8000).

### Usage

You may need to create a superuser account for administrative access.

#### Employee Hierarchy View
- URL: `/employees/hierarchy/`
- Description: View the hierarchical representation of employees.

#### Employee Detail View
- URL: `/employees/<int:pk>/`
- Description: View details of a specific employee.

#### Employee List View
- URL: `/employees/list/`
- Description: View a list of all employees.

#### Employee List (Home) View
- URL: `/employees/`
- Description: View the home page with a list of all employees.

#### Register User View
- URL: `/employees/register/`
- Description: Register a new user account.

#### Login User View
- URL: `/employees/login/`
- Description: Log in with an existing user account.

#### Logout User
- URL: `/employees/logout/`
- Description: Log out the current user.

#### Add Employee View (Create)
- URL: `/employees/add/`
- Description: Add a new employee.
- Note: Only registered users can perform this action.

#### Edit Employee View (Update)
- URL: `/employees/edit/<int:pk>/`
- Description: Edit details of an existing employee.
- Note: Only registered users can perform this action.

#### Delete Employee View
- URL: `/employees/delete/<int:pk>/`
- Description: Delete an existing employee.
- Note: Only registered users can perform this action.

#### Admin Interface
- URL: `/admin/`
- Description: Access the Django admin interface for managing data.

### Note
- To create, edit, or delete employees, users need to be registered and logged in.

### Additional Information

For more details or if you encounter any issues, please refer to the project documentation or contact the project maintainer.

## Authors

- Andrii Mikita
