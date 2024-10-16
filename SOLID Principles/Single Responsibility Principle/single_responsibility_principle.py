"""
Single Responsibility Principle

A class should be responsible for one thing only. If a class does too many things,
it's harder to change without breaking something else.
"""

class Employee:
    """
    The Employee class represents an employee with basic details like name and salary.

    Responsibilities:
    - Manage employee properties (name and salary).
    - Provide a method to retrieve employee details.
    """

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def get_details(self) -> str:
        """
        Get the details of the employee in a formatted string.

        Returns:
            str: Formatted details of the employee.
        """
        return f"Employee: {self.name}, Salary: {self.salary}"

    def save_to_database(self):
        """
        Simulate saving the employee to the database.
        """
        print(f"Saved employee {self.name} to the database.")

"""
The Employee class violates the SRP because it combines multiple responsibilities:
1. Managing employee properties.
2. Database management for employee.

The problem with using above approach is that any future changes to the employees database management could create a 
ripple effect across all components that rely on this class. As a result, those components would need to be 
updated to accommodate the changes and retested.

To solve this problem, we can break the class into two separate classes: one for managing employee details 
and another for handling employee database storage.
"""

class Employee:
    """
    The Employee class represents an employee with basic details like name and salary.

    Responsibilities:
    - Manage employee properties (name and salary).
    """

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def get_details(self) -> str:
        """
        Get the details of the employee in a formatted string.

        Returns:
            str: Formatted details of the employee.
        """
        return f"Employee: {self.name}, Salary: {self.salary}"

class EmployeeDB:
    """
    The EmployeeDB class is responsible for handling database operations related to employees.

    Responsibilities:
    - Save employee data to the database.
    - Delete employee data from the database.
    - Read employee data from the database.
    - Update employee data from the database.
    """

    def save(self, employee: Employee):
        """
        Simulate saving the employee to the database.

        Args:
            employee (Employee): The employee object to save.
        """
        print(f"Saved employee {employee.name} to the database.")

    def delete(self, employee: Employee):
        """
        Simulate deleting the employee from the database.

        Args:
            employee (Employee): The employee object to delete.
        """
        print(f"Deleted employee {employee.name} from the database.")

    def read(self, employee: Employee):
        """
        Simulate reading the employee from the database.

        Args:
            employee (Employee): The employee object to read.
        """
        print(f"Read employee {employee.name} from the database.")

    def update(self, employee: Employee):
        """
        Simulate updating the employee in the database.

        Args:
            employee (Employee): The employee object to update.
        """
        print(f"Updated employee {employee.name} in the database.")

"""
By separating responsibilities, the Employee class now solely manages employee data,
while the EmployeeDB class takes care of database operations. 

This design follows the Single Responsibility Principle, making the system more modular and easier to maintain.
"""

"""
However, the main drawback of using this solution is that clients must deal with both the Employee and EmployeeDB classes.

A common solution to this dilemma is to apply the Facade Pattern.
"""

"""
Below is an example for using the above defined classes
"""
employee = Employee("John Doe", 50000)

print(employee.get_details())

employee_db = EmployeeDB()
employee_db.save(employee)
