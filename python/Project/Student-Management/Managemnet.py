user_data = {}
student_dict = {}

def Add_Student():
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        print(f"\n--- Student {i+1} ---")
        student_id = int(input("Enter student ID: "))
        student_name = input("Enter student name: ").strip()
        num_subjects = int(input("Enter total number of subjects: "))

        subjects_dict = {}
        for j in range(num_subjects):
            subject_name = input(f"Enter name of subject {j+1}: ")
            grade = int(input(f"Enter grade for {subject_name}: "))
            subjects_dict[subject_name] = grade

        total = sum(subjects_dict.values())
        average = total / len(subjects_dict)

        user_data[student_id] = {
            "name": student_name,
            "subjects": subjects_dict,
            "total": total,
            "average": average
        }

        def Students_report():
    student_dict.clear()
    for key, value in user_data.items():
        AvgGrade = value['average']
        if 90 <= AvgGrade <= 100:
            student_dict[value['name']] = f"Student with id {key} got Grade A"
        elif 80 <= AvgGrade < 90:
            student_dict[value['name']] = f"Student with id {key} got Grade B"
        elif 70 <= AvgGrade < 80:
            student_dict[value['name']] = f"Student with id {key} got Grade C"
        else:
            student_dict[value['name']] = f"Student with id {key} Failed"

    print("\n--- All Student Reports ---")
    for name, result in student_dict.items():
        print(name, "->", result)


        
def Find_topper():
    if not user_data:
        print("No students available.")
        return

    topper = -1
    topperName = ""

    for value in user_data.values():
        if value['average'] > topper:
            topper = value['average']
            topperName = value['name']

    print("\n--- Topper Student ---")
    print(f"{topperName} got the highest average: {topper}")