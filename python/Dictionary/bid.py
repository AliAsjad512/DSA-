# print("\n" *100)
# input("Press Enter to continue...")

company = {
    "name": "TechCorp",
    "employees": [
        {"name": "Ali", "role": "Dev"},
        {"name": "Sara", "role": "QA"}
    ]
}

# print(company["employees"])
# print(company["employees"][1]["name"]["role"])
# for employee in company["employees"]:
#     if employee['role']=='Dev':
#      print(employee['name'],employee['role'])


     data = {
    "users": [
        {
            "id": 1,
            "skills": ["Python", "AWS"]
        }
    ]
}

print(data["users"][0]["id"][0])

company = {
    "employees": [
        {"name": "Ali", "skills": ["Python", "AWS"]},
        {"name": "Sara", "skills": ["Java", "SQL"]}
    ]
}
print(company["employees"][1]["skills"][0])

employee = {
    "emp1": {"name": "Ali", "role": "Dev"},
    "emp2": {"name": "Sara", "role": "QA"}
}


grades = {
    "Ali": {"Math": 85, "CS": 90},
    "Sara": {"Math": 78, "CS": 95}
}
for student, subjects in grades.items():
    print(student, subjects["Math"],subjects["CS"])



    
