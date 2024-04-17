import copy

students = ['james', 'mike', 'alfred']

print('students - ' + str(students) + '\n')

# copying list object
employees = copy.deepcopy(students)

print('employees - ' + str(employees) + '\n')

# modifying students
students.append('Shawn')

print('modified students - ' + str(students) + '\n')

print('employees - ' + str(employees) + '\n')


