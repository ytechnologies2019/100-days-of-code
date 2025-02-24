from collections.abc import dict_values
from multiprocessing.managers import Value

import pandas

student_dict = {
    "student" : ['Angela' , 'James' , 'Lilly'] ,
    "score" : [56,80,70]
}

# for (key , value) in student_dict.items():
#       print(key)
#     # print(value)

student_dataframe = pandas.DataFrame(student_dict)
#print (student_dataframe)

#Loop through the dataframe
for (index ,row) in student_dataframe.iterrows():
    if row.student == "Angela":
        print (row.score)

