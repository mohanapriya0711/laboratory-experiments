def find_occurrence(numbers, target):
    positive_indices = []
    negative_indices = []

    for i in range(len(numbers)):
        if numbers[i] == target:
            positive_indices.append(i)
            negative_indices.append(i - len(numbers))

    return positive_indices, negative_indices

numbers = list(map(int, input("Enter a list of numbers, separated by commas: ").split(",")))
target_number = int(input("Enter the element to be found: "))
positive_indices, negative_indices = find_occurrence(numbers, target_number)
occurrence = len(positive_indices)
print(f"Element {target_number} occurs {occurrence} times in the list.")
print("Positive Index :", ", ".join(map(str, positive_indices)))
print("Negative Index :", ", ".join(map(str, negative_indices)))