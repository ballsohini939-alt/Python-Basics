def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
name = input("Enter your name: ")
marks = float(input("Enter your marks: "))
grade = calculate_grade(marks)
print("\n--- Result ---")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)