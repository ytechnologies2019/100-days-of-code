##Create DataFrame
import pandas

data_dict = {
    "students" : ["Amy" , "Jame" , "Panda"] ,
    "scores" : [70 , 80 , 90]
}
change_dataframe = pandas.DataFrame(data_dict)
change_csv = change_dataframe.to_csv('student_list.csv')