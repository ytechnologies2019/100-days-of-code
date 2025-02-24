with open ('file1.txt') as file1:
    list1 = file1.readlines()

with open ('file2.txt') as file2:
    list2 = file2.readlines()

result = [int(same_num) for same_num in list1 if same_num in list2 ]
print (result)