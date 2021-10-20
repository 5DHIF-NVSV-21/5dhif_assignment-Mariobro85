"""
Nico Baumann
24th September 2021
"""

# employees.csv: id, name, department_id, hire_date
# departments.csv: id, name, location

# to define os-independent file paths
import os
# system date and time
from datetime import datetime as dt

"""
The `Department` class stores the ID, name and US-location of this department.
"""
class Department:
	def __init__(self, id, name, location):
		# unique id of the department
		self.id = id
		# unique name of the department
		self.name = name
		# location of the department
		# I'm using US cities only for simplicity
		self.location = location
		pass
	
	def get_id(self):
		return self.id
	
	def get_name(self):
		return self.name
	
	def get_location(self):
		return self.location
	
	def printf(self):
		print(f"{self.id} - {self.name}, {self.location.strip()}")
		pass
	
	def to_csv(self):
		return str(str(self.id) + "," + self.name + "," + self.location)



"""
The `Employee` class stores relevant information about an employee such as
their ID, name, current department and the hiring date.
"""
class Employee:
	def __init__(self, id, name, department_id, hiring_date_str):
		# unique id of the employee
		self.id = id
		# full name of the employee
		self.name = name
		# the department the employee is currently working in
		self.department = self.set_department_by_id(department_id)
		# the day the employee was hired, if null use today's date
		if hiring_date_str == None:
			self.hiring_date = dt.today()
		else:
			self.hiring_date = dt.strptime(hiring_date_str[0:10], "%d.%m.%Y").date()
		pass
	
	def get_id(self):
		return self.id
	
	def set_id(self, id):
		self.id = id
		pass
	
	def get_name(self):
		return self.name
		
	def set_name(self, name):
		self.name = name
		pass
	
	def get_department(self):
		return self.department
	
	def set_department_by_id(self, id):
		for dept in departments:
			if dept.id == id:
				return dept
			pass
		pass
	
	def get_hiring_date(self):
		return self.hiring_date
	
	def set_hiring_date(self, hiring_date):
		self.hiring_date = hiring_date
		pass
	
	def printf(self):
		print(f"{self.id} - {self.name}, working in {self.department.get_name()} ({self.department.get_location().strip()}), hired on {self.hiring_date.strftime('%d.%m.%Y')}")
		pass
	
	def to_csv(self):
		return str(str(self.id) + "," + self.name + "," + str(self.department.get_id()) + "," + self.hiring_date.strftime("%d.%m.%Y") + "\n")


# full list of employees
employees = []

# full list of departments
departments = []



"""
Reads the given file as .csv.

:param filename: the name of the file
:param colums: How many columns the .csv file contains
:return: the file content in an array
"""
def read_csv_file(filename):
	# create full file path using the given name
	# os.path.dirname(...) is the directory this script is located in
	filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "res_p01", filename)
	# open the file
	csv_file = open(filepath, "r")
	# save content as list
	content = csv_file.readlines()
	
	# close file and return content
	csv_file.close()
	return content

"""
Saves the given string array as .csv file.

:param filename: the name of the file
:param data: The data to write
"""
def save_csv_file(filename, data):
	# create full file path using the given name
	# os.path.dirname(...) is the directory this script is located in
	filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "res_p01", filename)
	# open the file
	csv_file = open(filepath, "w")
	# save content as list
	for line in data:
		csv_file.write(line)
	
	# close file and return content
	csv_file.close()
	pass

"""
Converts the array from `read_csv_file()` to a list of Departments

:param arr: The data array
:return: The list of departments
"""
def array_to_department_list(arr):
	dept_list = []
	
	for line in arr:
		parts = line.split(",")
		dept_list.append(Department(int(parts[0]), parts[1], parts[2]))
	
	return dept_list

"""
Converts the array from `read_csv_file()` to a list of Employee

:param arr: The data array
:return: The list of employees
"""
def array_to_employee_list(arr):
	emp_list = []
	
	for line in arr:
		parts = line.split(",")
		emp_list.append(Employee(int(parts[0]), parts[1], int(parts[2]), parts[3]))
	
	return emp_list

"""
Prints the information of selected employee via ID

:param id: the employee id
"""
def print_emp(id):
	emp = None
	for e in employees:
		if e.get_id() == id:
			emp = e
			break
	
	if emp != None:
		emp.printf()
	else:
		print(f"Employee #{id} not found.")
	
	pass

"""
Prints all the information about every currently registered employee.
"""
def print_all():
	for emp in employees:
		emp.printf()
	pass

"""
Hires a new employee

:param employee: The employee to hire
"""
def add_emp(employee):
	employees.__add__(employee)
	print("Employee successfully added.")
	pass

"""
Fires the employee with the corresponding ID

:param id: The ID of the employee to remove
"""
def delete_emp(id):
	emp = None
	
	for e in employees:
		if e.get_id() == id:
			emp = e
			break
	
	if emp != None:
		employees.remove(emp)
		print("Successfully fired employee:")
		emp.printf()
	else:
		print(f"Employee #{id} not found.")
	
	pass

"""
Lets user modify an employees information wihtout needing to fire an rehire them

:param id: The id of the employee to modify
"""
def modify_emp(id):
	for emp in employees:
		if emp.get_id() == id:
			print(f" Modify Employee #{emp.get_id()}")
			
			try:
				# just get user input for now
				# name
				print(f"Current Name: {emp.get_name()}")
				new_name = input("Change to: ").strip() # .strip() removes leading/trailing spaces/tabs/new lines
				# department
				print("Available Departments:")
				print_departments()
				print("Current Dept.: ", end = "")
				emp.get_department().printf()
				new_dept = int(input("Change to: "))
				# hire date
				print(f"Hired on: {emp.get_hiring_date().strftime('%d.%m.%Y')}")
				new_hdate_str = input("Change to (DD.MM.YYYY): ").strip()
				
				# now it's safe to set the variables (if necessary) - user entered everything correctly
				emp.set_name(new_name)
				emp.set_department_by_id(new_dept)
				
				new_hdate = dt.strptime(new_hdate_str, "%d.%m.%Y")
				emp.set_hiring_date(new_hdate)
				
				print("\nData successfully modified:")
				emp.printf()
			except:
				print("Invalid input. Aborting...")
			break
	pass

"""
Prints all currently known departments.
"""
def print_departments():
	for dept in departments:
		dept.printf()
	pass

"""
Checks for already existing ID.

:param id: The id to check
"""
def check_emp_id(id):
	for emp in employees:
		if emp.get_id() == id:
			return True
	
	return False

"""
Checks if department exists.

:param id: The department to check
"""
def check_dept_id(id):
	for dept in departments:
		if dept.get_id() == id:
			return True
	
	return False



"""
The Main Loop
"""
if __name__ == '__main__':
	# get all departments
	departments = array_to_department_list(read_csv_file("departments.csv"))
	# get all employees
	employees = array_to_employee_list(read_csv_file("employees.csv"))
	
	# loop until user exits
	while True:
		# print all options
		print()
		print(30 * "-")
		print("What do you want to do?")
		print("1) Print Employee")
		print("2) Print All Employees")
		print("3) Add Employee")
		print("4) Delete Employee")
		print("5) Change Employee's Data")
		print("6) Save and Exit")
		print("7) Exit without Saving")
		
		# check user input for errors
		try:
			selected = int(input("> "))
		except:
			print("Invalid input. Please try again.")
			continue
		
		if   selected == 1:
			id = int(input("Employee ID: "))
			print_emp(id)
			pass
			
		elif selected == 2:
			print_all()
			pass
			
		elif selected == 3:
			try:
				while True:
					id = int(input("ID: ").strip())
					if check_emp_id(id):
						print("This ID already exists. Please enter another.")
						continue
					else: break
				
				name = input("Full Name: ").strip()
				
				while True:
					print("Available departments:")
					print_departments()
					dept = int(input("Dept. ID: ").strip())
					
					if check_dept_id(dept) == False:
						print("Invalid department. Please try again.")
						continue
					else: break
				
				emp = Employee(id, name, dept, None)
				print("Successfully added new employee:")
				emp.printf()
				employees.append(emp)
			except:
				print("Invalid input.")
			pass
		
		elif selected == 4:
			try:
				id = int(input("Employee ID: "))
				delete_emp(id)
			except:
				print("Invalid Input.")
			pass
		
		elif selected == 5:
			try:
				id = int(input("Employee ID: ").strip())
				modify_emp(id)
			except:
				print("Invalid Input.")
			pass
		
		elif selected == 6:
			write_data = []
			for emp in employees:
				write_data.append(emp.to_csv())
			
			save_csv_file("employees.csv", write_data)
			exit()
		
		elif selected == 7:
			print("\n" + (52 * "="))
			confirm = input("Are you sure you want to exit without saving? (y/n)\n" + (52 * "=") + "\n").strip().lower()
			
			if confirm == "y" or confirm == "yes":
				exit()
			elif confirm == "n" or confirm == "no":
				continue
			else:
				print("Invalid input, aborting...")
				continue
		
		else: continue
