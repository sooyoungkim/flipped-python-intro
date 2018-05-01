from collections import namedtuple
import csv

f = open("resources/users.csv", "r")
next(f)

reader = csv.reader(f)
student_list = []
for row in reader:
    # print(row)
    student_list.append(row)

# print(student_list)


columns = ["user_id", "integration_id", "login_id", "password", "first_name",
            "last_name", "full_name", "sortable_name", "short_name",
            "email", "status"]
Student = namedtuple('Student', columns)

student_namedtupe_list = []
for row in student_list:
    # argument인 row를 unpacking - list에 있는 원소를 하나씩 꺼낸다.
    student = Student(*row)
    student_namedtupe_list.append(student)

print(student_namedtupe_list[0])
# Student(user_id='1555551', integration_id='', login_id='lrice', password='', first_name='Lonnie', last_name='Rice', full_name='Lonnie Rice', sortable_name='Rice, Lonnie', short_name='Lonnie Rice', email='lrice@institution-name.edu', status='active')
print(student_namedtupe_list[0].full_name)
# Lonnie Rice
