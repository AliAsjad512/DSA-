user_data = {}
student_dict = {}

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    print(f"\n--- Student {i+1} ---")

    student_id = int(input("Enter student ID: "))

    # ✅ Validate student name (string only)
    while True:
        student_name = input("Enter student name: ").strip()
        if student_name.replace(" ", "").isalpha():
            break
        else:
            print("❌ Invalid input. Student name must contain letters only.")

    num_subjects = int(input("Enter total number of subjects: "))

    subjects_dict = {}

    for j in range(num_subjects):
        # ✅ Validate subject name (string only)
        while True:
            subject_name = input(f"Enter name of subject {j+1}: ").strip()
            if subject_name.replace(" ", "").isalpha():
                break
            else:
                print("❌ Invalid input. Subject name must contain letters only.")

        grade = int(input(f"Enter grade for {subject_name}: "))
        subjects_dict[subject_name] = grade

    total = sum(subjects_dict.values())
    average = total / len(subjects_dict)

    print("Your average score is:", average)

    user_data[student_id] = {
        "name": student_name,
        "subjects": subjects_dict,
        "total": total,
        "average": average
    }

# Clear previous results
student_dict.clear()

# Assign grades
for student_id, value in user_data.items():
    AvgGrade = value['average']
    name = value['name']

    if 90 <= AvgGrade <= 100:
        student_dict[name] = f"Student with id {student_id} got Grade A"
    elif 80 <= AvgGrade <= 89:
        student_dict[name] = f"Student with id {student_id} got Grade B"
    elif 70 <= AvgGrade <= 79:
        student_dict[name] = f"Student with id {student_id} got Grade C"
    else:
        student_dict[name] = f"Student with id {student_id} Failed"

print("\n--- Student Grades ---")
for name, result in student_dict.items():
    print(name, "->", result)

    for key, value in user_data.items():
  highGrade=value['average']
  if highGrade > topper:
    topper=highGrade
    toppperName=value['name']

print("\n--- Topper Student---")
print("Student who got highest grade in class ", topper,toppperName)

print("\n Search Student by their Id ")
StdId=int(input('Enter student id'))

for k, val in user_data.items():
  if k==StdId:
    print(val)
