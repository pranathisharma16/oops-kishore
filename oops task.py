from abc import ABC, abstractmethod
from typing import List


class Employee(ABC):

    def __init__(self, employeeId, name, salary, department):
        self.employeeId = employeeId
        self.name = name
        self.salary = float(salary)
        self.department = department  

        
        self.email = f"{self.name.lower()}@{self.department.lower()}.company.com"

    @abstractmethod
    def calculateBonus(self):
        pass


    @abstractmethod
    def get_employee_type(self):
        pass

    def displayDetails(self):
        print(f"""
Employee Details:
  ID         : {self.employeeId}
  Name       : {self.name}
  Salary     : {self.salary}
  Department : {self.department}
  Email      : {self.email}
  Type       : {self.get_employee_type()}
""")


class payable(ABC):
    @abstractmethod
    def process_salary(self):
        pass


class fullTimeEmployee(Employee, payable):

    def __init__(self, employeeId, name, salary, bonusPercentage, department):
        super().__init__(employeeId, name, salary, department)
        self.bonusPercentage = float(bonusPercentage)

    def calculateBonus(self):
        return self.salary * (self.bonusPercentage / 100.0)

    def process_salary(self):
        total = self.salary + self.calculateBonus()
        print(f"Salary for {self.name} (FTE): Total = {total} (Bonus = {self.calculateBonus()})")

    def get_employee_type(self):
        return "Full Time"


class partTimeEmployee(Employee, payable):

    def __init__(self, employeeId, name, hourly_rate, hours_worked, bonusPercentage, department):
        super().__init__(employeeId, name, 0, department)
        self.hourly_rate = float(hourly_rate)
        self.hours_worked = hours_worked
        self.bonusPercentage = float(bonusPercentage)

    def pay(self):
        return self.hourly_rate * self.hours_worked

    def calculateBonus(self):
        return self.pay() * (self.bonusPercentage / 100.0)

    def process_salary(self):
        total = self.pay() + self.calculateBonus()
        print(f"Salary for {self.name} (PTE): Total = {total} (Bonus = {self.calculateBonus()})")

    def get_employee_type(self):
        return "Part Time"


def main():
    ft = fullTimeEmployee(
        employeeId=101, 
        name="Abhay", 
        salary=10000, 
        bonusPercentage=10, 
        department="IT"
    )

    pt = partTimeEmployee(
        employeeId=202, 
        name="Samay", 
        hourly_rate=500, 
        hours_worked=50, 
        bonusPercentage=20, 
        department="HR"
    )

    employees: List[Employee] = [ft, pt]


    for e in employees:
        e.displayDetails()
        print(f"Bonus = {e.calculateBonus()}")
       
    payroll: List[payable] = [ft, pt]
    for p in payroll:
        p.process_salary()


if __name__ == "__main__":
    main()