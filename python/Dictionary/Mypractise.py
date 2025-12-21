
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

for skill in response['data']['users']:
 for key,value in skill.items():
  if(key=='skills'):
    for language in value:
      print(language)

      grades = {
    "Ali": {"Math": 85, "CS": 90},
    "Sara": {"Math": 78, "CS": 95}
}

for student, subjects in grades.items():
    print(student, subjects["CS"])



company = {
    "HR": ["Ali", "Sara"],
    "IT": ["John", "Emma"]
}

for dept, employees in company.items():
    print("Department:", dept)
    for emp in employees:
        print(emp)

        d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
 print('A {} has {} legs'.format(animal, legs))

 # Initialize an empty dictionary
user_data = {}

# Ask the user how many entries they want to add
num_entries = int(input("Enter the number of entries: "))

# Loop 'num_entries' times to get key-value pairs
for _ in range(num_entries):
    key = input("Enter a key: ")
    # Input is always a string; use int() or float() if you need other types
    value = input("Enter the value for the key: ")
    user_data[key] = value # Assign the value to the key

# Print the resulting dictionary
print(user_data)

