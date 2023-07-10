def is_subset(set_a, set_b):
    for element in set_a:
        if element not in set_b:
            return False
    return True
a = {1, 2, 3, 4}
b = {1, 2, 3}
is_subset = is_subset(a, b)
print(is_subset)