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