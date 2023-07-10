n = int(input("Enter number of elements in a list: "))
num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)
try:
    index = int(input("Enter the index value: "))
    element = num_list[index]
    print("Element at index", index, "is", element)
except IndexError:
    last_index = len(num_list) - 1
    print("Index is not present, the last index value is", last_index)