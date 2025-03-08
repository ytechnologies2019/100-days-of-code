from typing import final

try:
    f = open('my_file.txt' , 'r')
    a_dictionary = {"key":"value"}
    print (a_dictionary["key"])

except FileNotFoundError:
    file = open('my_file.txt' , 'w')
    file.write('Text')

except KeyError as error_message:
    print(f"The key {error_message} not found")

else:
    content = f.read()
    print(content)

finally:
    f.close()
    print("File was closed")
    raise FileNotFoundError("This is fake error")


