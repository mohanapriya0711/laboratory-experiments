def is_ascending_order(list_nums):
  for i in range(len(list_nums) - 1):
    if list_nums[i] > list_nums[i + 1]:
      return False
  return True

def main():
  num_elements = int(input("Enter number of elements in list: "))
  list_nums = []
  for i in range(num_elements):
    value = int(input("Enter the value - "))
    list_nums.append(value)
  print("Original list: ", list_nums)
  if is_ascending_order(list_nums):
    print("Yes, the list is in ascending order.")
  else:
    print("No, the list is not in ascending order.")

if __name__ == "__main__":
  main()
