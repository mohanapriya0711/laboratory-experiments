with open("File2.txt", "r") as file2:
    content = file2.readlines()
with open("File1.txt", "a") as file1:
    file1.writelines(content)
print("Content from File 2 has been appended to File 1.")