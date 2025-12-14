
response = {
    "status": 200,
    "data": {
        "users": [
            {
                "id": 1,
                "name": "Ali",
                "skills": ["Python", "AWS"]
            },
            {
                "id": 2,
                "name": "Sara",
                "skills": ["Java", "SQL"]
            }
        ]
    }
}

for skill in response['data']['users']['skills']:
  print(skill)


# #print the subject "Physics" from the list of subjects in the dictionary
# student = {
#     "name": "Ali",
#     "subjects": ["Math", "Physics", "CS"]
# }

# print(student["subjects"][1])


# students = [
#     {"name": "Ali", "age": 25},
#     {"name": "Sara", "age": 24}
# ]
# print(students[1]["age"])


# employee = {"emp1": {"name": "Ali", "role": "Dev"}}
# employee["emp1"]["salary"] = 70000
# print(employee)

# #update data of first student 
# students = [
#     {"name": "Ali", "marks": 85},
#     {"name": "Sara", "marks": 92}
# ]
# students[0]["name"]="Asjad"
# students[0]["marks"]=100
# for student in students:
#  print(student)


