from datetime import datetime, date
from enum import Enum
from typing import Dict, List, Optional


class LeaveType(Enum):
    ANNUAL = "Annual Leave"
    SICK = "Sick Leave"
    UNPAID = "Unpaid Leave"


class LeaveStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class Employee:
    def __init__(self, employee_id: int, name: str, email: str, department: str, 
                 position: str, hire_date: date, manager_id: Optional[int] = None):
        self.id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.position = position
        self.hire_date = hire_date
        self.manager_id = manager_id
        self.is_active = True
        
    def __str__(self) -> str:
        return f"{self.name} - {self.position} ({self.department})"


class LeaveRequest:
    def __init__(self, request_id: int, employee_id: int, leave_type: LeaveType, 
                 start_date: date, end_date: date, reason: str):
        self.id = request_id
        self.employee_id = employee_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
        self.status = LeaveStatus.PENDING
        self.reviewed_by = None
        self.comments = None
        
    @property
    def duration(self) -> int:
        """Calculate the number of days for the leave."""
        delta = self.end_date - self.start_date
        return delta.days + 1


class HRSystem:
    def __init__(self):
        self.employees = {}  # employee_id -> Employee
        self.leave_requests = {}  # request_id -> LeaveRequest
        self.leave_balances = {}  # (employee_id, year) -> Dict[LeaveType, int]
        self.next_employee_id = 1
        self.next_request_id = 1
        
    def add_employee(self, name: str, email: str, department: str, 
                    position: str, hire_date: date, manager_id: Optional[int] = None) -> int:
        """Add a new employee to the system."""
        employee_id = self.next_employee_id
        self.next_employee_id += 1
        
        employee = Employee(employee_id, name, email, department, position, hire_date, manager_id)
        self.employees[employee_id] = employee
        
        # Initialize leave balances
        current_year = date.today().year
        self.leave_balances[(employee_id, current_year)] = {
            LeaveType.ANNUAL: 20,  # Default annual leave
            LeaveType.SICK: 10,    # Default sick leave
            LeaveType.UNPAID: float('inf')  # Unlimited unpaid leave
        }
        
        return employee_id
        
    def get_employee(self, employee_id: int) -> Optional[Employee]:
        """Get employee by ID."""
        return self.employees.get(employee_id)
    
    def get_all_employees(self) -> List[Employee]:
        """Get all active employees."""
        return [emp for emp in self.employees.values() if emp.is_active]
    
    def get_employees_by_department(self, department: str) -> List[Employee]:
        """Get all employees in a department."""
        return [emp for emp in self.employees.values() 
                if emp.department == department and emp.is_active]
    
    def update_employee(self, employee_id: int, **kwargs) -> bool:
        """Update employee information."""
        if employee_id not in self.employees:
            return False
        
        employee = self.employees[employee_id]
        
        for key, value in kwargs.items():
            if hasattr(employee, key):
                setattr(employee, key, value)
        
        return True
    
    def terminate_employee(self, employee_id: int) -> bool:
        """Mark an employee as inactive (terminated)."""
        if employee_id not in self.employees:
            return False
        
        self.employees[employee_id].is_active = False
        return True
    
    def request_leave(self, employee_id: int, leave_type: LeaveType, 
                      start_date: date, end_date: date, reason: str) -> Optional[int]:
        """Submit a leave request."""
        if employee_id not in self.employees or not self.employees[employee_id].is_active:
            return None
        
        request_id = self.next_request_id
        self.next_request_id += 1
        
        leave_request = LeaveRequest(request_id, employee_id, leave_type, 
                                    start_date, end_date, reason)
        self.leave_requests[request_id] = leave_request
        
        return request_id
    
    def process_leave_request(self, request_id: int, status: LeaveStatus, 
                             reviewer_id: int, comments: Optional[str] = None) -> bool:
        """Process (approve or reject) a leave request."""
        if request_id not in self.leave_requests:
            return False
        
        if reviewer_id not in self.employees:
            return False
        
        leave_request = self.leave_requests[request_id]
        current_year = leave_request.start_date.year
        
        # Check if the reviewer is the manager of the employee
        employee = self.employees[leave_request.employee_id]
        if employee.manager_id != reviewer_id:
            return False
        
        if status == LeaveStatus.APPROVED:
            # Check leave balance
            balance_key = (leave_request.employee_id, current_year)
            
            if balance_key not in self.leave_balances:
                self.leave_balances[balance_key] = {
                    LeaveType.ANNUAL: 20,
                    LeaveType.SICK: 10,
                    LeaveType.UNPAID: float('inf')
                }
            
            # Only check balance for leave types that are limited
            if leave_request.leave_type != LeaveType.UNPAID:
                balance = self.leave_balances[balance_key][leave_request.leave_type]
                used = self.get_used_leave(leave_request.employee_id, leave_request.leave_type, current_year)
                
                if balance - used < leave_request.duration:
                    return False  # Not enough leave balance
        
        leave_request.status = status
        leave_request.reviewed_by = reviewer_id
        leave_request.comments = comments
        
        return True
    
    def get_leave_requests(self, employee_id: Optional[int] = None, 
                          status: Optional[LeaveStatus] = None) -> List[LeaveRequest]:
        """Get leave requests filtered by employee and/or status."""
        requests = self.leave_requests.values()
        
        if employee_id is not None:
            requests = [req for req in requests if req.employee_id == employee_id]
        
        if status is not None:
            requests = [req for req in requests if req.status == status]
        
        return list(requests)
    
    def get_leave_balance(self, employee_id: int, leave_type: LeaveType, 
                         year: Optional[int] = None) -> float:
        """Get remaining leave balance for an employee."""
        if not year:
            year = date.today().year
        
        balance_key = (employee_id, year)
        
        if balance_key not in self.leave_balances:
            return 0
        
        total_balance = self.leave_balances[balance_key][leave_type]
        used_leave = self.get_used_leave(employee_id, leave_type, year)
        
        return total_balance - used_leave
    
    def get_used_leave(self, employee_id: int, leave_type: LeaveType, 
                      year: int) -> int:
        """Calculate used leave days for a specific type and year."""
        used_days = 0
        
        for request in self.leave_requests.values():
            if (request.employee_id == employee_id and 
                request.leave_type == leave_type and 
                request.status == LeaveStatus.APPROVED and 
                request.start_date.year == year):
                used_days += request.duration
        
        return used_days
    
    def adjust_leave_balance(self, employee_id: int, leave_type: LeaveType, 
                            year: int, days: int) -> bool:
        """Adjust leave balance (add or subtract days)."""
        if employee_id not in self.employees:
            return False
        
        balance_key = (employee_id, year)
        
        if balance_key not in self.leave_balances:
            self.leave_balances[balance_key] = {
                LeaveType.ANNUAL: 20,
                LeaveType.SICK: 10,
                LeaveType.UNPAID: float('inf')
            }
        
        self.leave_balances[balance_key][leave_type] += days
        return True


# Example usage
if __name__ == "__main__":
    # Initialize the HR system
    hr_system = HRSystem()
    
    # Add employees
    manager_id = hr_system.add_employee(
        "Alice Smith", "alice@example.com", "Management", 
        "Department Manager", date(2015, 5, 10)
    )
    
    emp1_id = hr_system.add_employee(
        "Bob Johnson", "bob@example.com", "Engineering", 
        "Software Engineer", date(2020, 3, 15), manager_id
    )
    
    emp2_id = hr_system.add_employee(
        "Charlie Brown", "charlie@example.com", "Engineering", 
        "QA Engineer", date(2021, 7, 1), manager_id
    )
    
    # Request leave
    today = date.today()
    start_date = date(today.year, today.month + 1 if today.month < 12 else 1, 5)
    end_date = date(today.year, today.month + 1 if today.month < 12 else 1, 10)
    
    request_id = hr_system.request_leave(
        emp1_id, LeaveType.ANNUAL, start_date, end_date, "Vacation"
    )
    
    # Approve leave
    hr_system.process_leave_request(
        request_id, LeaveStatus.APPROVED, manager_id, "Approved"
    )
    
    # Print employee info
    print("Employees:")
    for emp in hr_system.get_all_employees():
        print(f"  {emp}")
    
    # Print leave balances
    print("\nLeave Balances:")
    for emp_id in [emp1_id, emp2_id]:
        emp = hr_system.get_employee(emp_id)
        print(f"  {emp.name}:")
        for leave_type in LeaveType:
            balance = hr_system.get_leave_balance(emp_id, leave_type)
            print(f"    {leave_type.value}: {balance}")
    
    # Print leave requests
    print("\nLeave Requests:")
    for request in hr_system.get_leave_requests():
        emp = hr_system.get_employee(request.employee_id)
        print(f"  {emp.name}: {request.start_date} to {request.end_date} - {request.status.value}")