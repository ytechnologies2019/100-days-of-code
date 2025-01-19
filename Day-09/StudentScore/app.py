student_score = {
    "Kimmy" : 100,
    "Harry" : 81 ,
    "Ron" : 78 ,
    "Hermione" : 99 ,
    "Draco" : 74 ,
    "Neville": 62
}
# TODO-1: Create an empty dictionary called student_grades
student_grade = {}

## TODO-2: Add the Grade to the student_acceptable_score
for student in student_score:
     if student_score[student] >= 91 or student_score[student] == 100:
         print (student + " is outstanding student")
     elif student_score[student] >= 81:
         print (student + " is exceed exceptions")
     elif student_score[student] >= 71:
         print (student + " is acceptable")
     else:
         print (student + " is failed")
