def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def count_digits(n):
    return len(str(n))

number = int(input("Enter an integer: "))

if number % 2 != 0:  # Odd number
    fact = factorial(number)
    digits = count_digits(fact)
    print(f"The factorial of {number} is: {fact}")
    print(f"The number of digits in the factorial is: {digits}")
else:  # Even number
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")