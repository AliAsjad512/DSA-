# student = {"name": "Ali", "age": 25}

# for key, value in student.items():
#     print(key, ":", value)
users = [
    {"name": "Ali", "role": "Dev","skills":{"Python":5,"AWS":3}},
    {"name": "Sara", "role": "QA","skills":{"Java":3,"SQL":5}}
]
for user in users:
 for key, value in user["skills"].items():
    if value>=4:
     print(user["name"],"has",key,"skill with level",value)
# for user in users:
#     print(user["name"], "is a", user["role"], "and has skills:", user["skills"])