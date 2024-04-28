# Assignment 14

# Create an Employee class
class Employee:
    # Constructor to initialize attributes
    def __init__(self, first_name="N/A", last_name="N/A", job_level=1, annual_salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.job_level = job_level
        self.annual_salary = annual_salary
        self.short_term_bonus = self.calculate_short_term_bonus()
        self.long_term_bonus = self.calculate_long_term_bonus()

    # Method to calculate short term bonus
    def calculate_short_term_bonus(self):
        if self.job_level == 1:
            return self.annual_salary * 0.25
        elif self.job_level == 2:
            return self.annual_salary * 0.20
        elif self.job_level == 3:
            return self.annual_salary * 0.10
        else:
            return 0

    # Method to calculate long term bonus
    def calculate_long_term_bonus(self):
        return self.annual_salary * 0.10

    # Method to display all attributes
    def display_info(self):
        print("\nFirst Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Job Level:", self.job_level)
        print("Annual Salary:", self.annual_salary)
        print("Short Term Bonus:", self.short_term_bonus)
        print("Long Term Bonus:", self.long_term_bonus)
        

# Create a Manager class inheriting from Employee
class Manager(Employee):
 
    def __init__(self, first_name, last_name, job_level, annual_salary, auto="N/A"):
        super().__init__(first_name, last_name, job_level, annual_salary)
        self.auto = auto

    # Overriding the calculate_long_term_bonus method for managers
    def calculate_long_term_bonus(self):
        if self.job_level == 1:
            return self.annual_salary * 0.50
        elif self.job_level == 2:
            return self.annual_salary * 0.40
        elif self.job_level == 3:
            return self.annual_salary * 0.35
        else:
            return 0 
        
    # Method to display all attributes including auto
    def display_info(self):
        super().display_info()
        print("Automobile:", self.auto)
        
# Instantiate the Manager object, load it with data, and display all the data
def main():
    
    # Create a regular employee object
    employee_1 = Employee("Jane", "Smith", 1, 60000)
    employee_2 = Employee("Bob", "Walker", 2, 60000)
    employee_3 = Employee("Andrew", "Gonzalez", 3, 60000)

    # Display information for the regular employee
    print("Employee Information:")
    employee_1.display_info()
    employee_2.display_info()
    employee_3.display_info()
    
    # Create a Manager object
    manager_1 = Manager("John", "Bear", 1, 60000, " Tesla")
    manager_2 = Manager("Alex", "Smith", 2, 60000, )
    manager_3 = Manager("Jane", "Dear", 3, 60000, " Lexus")


    # Display information for the manager
    print("\nManager Information:")
    manager_1.display_info()
    manager_2.display_info()
    manager_3.display_info()
  

# Call the main function
if __name__ == "__main__":
    main()
