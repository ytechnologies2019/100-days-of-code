import random
from tkinter.font import names

names = {
    "Alex" : 89 ,
    "Beth" : 98
}

students_score = {student:random.randint(1, 100) for student in names}
print (students_score)

passed_students = {student:students_score for (student, students_score) in students_score.items() if students_score >= 60}
print (passed_students)