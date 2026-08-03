def calculate_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)
marks = []
number_of_subjects = int(input("Enter number of subjects: "))
for i in range(number_of_subjects):
    mark = float(input("Enter marks: "))
    marks.append(mark)
average = calculate_average(marks)
print("\n--- Result ---")
print("Marks:", marks)
print("Average:", average)
if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")