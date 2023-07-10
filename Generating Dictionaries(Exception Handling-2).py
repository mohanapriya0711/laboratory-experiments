class NegativeAgeError(Exception):
    pass

def create_student_dict():
    details = {}
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 0:
        raise NegativeAgeError("Age can't be a negative value")

    marks = []
    print("Enter 6 subject marks:")
    for _ in range(6):
        mark = int(input())
        marks.append(mark)

    details["Name"] = name
    details["Age"] = age
    details["Marks"] = marks
    details["Total"] = sum(marks)
    details["Average"] = sum(marks) / len(marks)

    return details


try:
    student_dict = create_student_dict()
    print(student_dict)
except NegativeAgeError as e:
    print(e)
    print("{}")