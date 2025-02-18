from os import write

with open("my_file.txt" , mode="a") as f:
    content = f.write("\nWrote by Python")
    print(content)
    f.close()