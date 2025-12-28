n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    m = int(input(f"Enter marks for student {i+1}: "))
    marks.append(m)

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks) / n)

for i, m in enumerate(marks):
    if m >= 90:
        grade = "A"
    elif m >= 75:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Student {i+1}: Grade {grade}")
