#Assignment 13

# Create employee class
class Employee:
    def __init__(self, first_name="N/A", last_name="N/A", job_level=1, annual_salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.job_level = job_level
        self.annual_salary = annual_salary
        self.short_term_bonus = 0
        self.long_term_bonus = 0
        self.calculate_bonuses()

    def calculate_bonuses(self):
        if self.job_level == 1:
            self.short_term_bonus = 0.25 * self.annual_salary
        elif self.job_level == 2:
            self.short_term_bonus = 0.20 * self.annual_salary
        elif self.job_level == 3:
            self.short_term_bonus = 0.10 * self.annual_salary
        self.long_term_bonus = 0.10 * self.annual_salary

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Job Level:", self.job_level)
        print("Annual Salary:", self.annual_salary)
        print("Short Term Bonus:", self.short_term_bonus)
        print("Long Term Bonus:", self.long_term_bonus)


# Instantiate an Employee object and display its information
emp1 = Employee()
emp2 = Employee("Perla", "Gonzalez", 2, 50000)
emp3 = Employee("Andrew", "Alvarez", 1, 45000)
emp4 = Employee("Jenny", "Sandoval", 3, 35000)
emp1.display_info()
emp2.display_info()
emp3.display_info()
emp4.display_info()
