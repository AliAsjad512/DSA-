# print("\n" *100)
# input("Press Enter to continue...")

company = {
    "name": "TechCorp",
    "employees": [
        {"name": "Ali", "role": "Dev"},
        {"name": "Sara", "role": "QA"}
    ]
}

#print(company["employees"][1]["name"]["role"])
for employee in company["employees"]:
    print(f"Employee Name: {employee['name']}, Role: {employee['role']}")
