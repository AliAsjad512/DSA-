



#print the subject "Physics" from the list of subjects in the dictionary
student = {
    "name": "Ali",
    "subjects": ["Math", "Physics", "CS"]
}

print(student["subjects"][1])


students = [
    {"name": "Ali", "age": 25},
    {"name": "Sara", "age": 24}
]
print(students[1]["age"])


employee = {"emp1": {"name": "Ali", "role": "Dev"}}
employee["emp1"]["salary"] = 70000
print(employee)