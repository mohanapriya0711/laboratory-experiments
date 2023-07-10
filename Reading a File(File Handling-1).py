n = int(input("Enter the number of lines to be read from the file: "))
with open("sample_file.txt", "r") as file:
    lines = [next(file).strip() for _ in range(n)]
for line in lines:
    print(line)