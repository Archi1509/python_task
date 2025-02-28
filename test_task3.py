from sre_constants import error


class Employee:
    def __init__(self):
        self.employees=employees_data
        self.name=name
        self.employee_id=employee_id
        self.salary=salary
        self.role=role
        self.extra_info=extra_info

    def display_all_employees(self):
        for name,info in self.employees.items():
            for employee_id,(role,salary,extra_info) in info.items():
                print(f"Name: {name} , Employee_id: {employee_id} ,Role: {role} ,Salary: {salary} ,Department: {extra_info} ")

    def filter_by_role(self,role_name):
        filter_role=[]
        for name,info in self.employees.items():
            for employee_id, (role, salary, extra_info) in info.items():
                if role==role_name:
                    filter_role.extend((name,salary))
        print(f"Applied Filter based on {role_name}:")
        print(filter_role)

    def filter_by_salary(self):
        filter_salary=[]
        min_salary=int(input("Enter Minimum Salary:"))
        max_salary=int(input("Enter Maximum Salary:"))
        for name,info in self.employees.items():
            for eid, (role, salary, extra_info) in info.items():
                if min_salary <= int(salary) <= max_salary:
                    filter_salary.extend([name,salary])


        print(f"Applied Filter based on Salary between range {min_salary} to {max_salary}:")
        print(filter_salary)

employees_data={}
f=1
while f:
    n=int(input("enter the number of employees"))
    for i in range(n):
        name=input("Enter name:")
        employee_id=input("Enter employee_id:")
        role=input("Enter role:")
        salary=input("Enter Salary:")
        extra_info=input("Enter the following details:\n department for managers(DM) or programming language for developers.(PID)\n")
        employees_data[name]={employee_id:[role,salary,extra_info]}
    a=input("Do You Want to Continue adding employee?(Yes/No)")

    if a=="No":
        f=0
    else:
        f=1
print(employees_data)

e=Employee()
e.display_all_employees()
e.filter_by_role("Developer")
e.filter_by_salary()

