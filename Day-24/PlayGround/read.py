with open("my_file.txt") as f:
    content = f.read()
    print(content)
    f.close()  #Close the file from background process
