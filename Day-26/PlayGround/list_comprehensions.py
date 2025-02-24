number = [1, 2, 3]
new_list = [n + 1 for n in number]
print(new_list)

name = "James"
letter_list = [letter for letter in name]
print (letter_list)

range_list = [num * 2 for num in range(1,5)]
print (range_list)

names      = ["James" , "Caroline" , "Tracer" , "Nancy" , "Mary"]
sort_names = [sort_name for sort_name in names if len(sort_name) < 5]
long_name  = [sort_name.upper() for sort_name in names if len(sort_name) < 5]
print (sort_names)
print(long_name)

# Old Method
# for n in number:
#     add_1 = n + 1
#     new_list.append(add_1)
#     print(new_list)
