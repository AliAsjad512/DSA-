tasks = {}
n = int(input("Enter the number of entries: "))

for _ in range(n):
    key = input("Enter key: ")
    title = float(input("Enter title: "))
    priority = input("Enter priority (high/medium/low): ")
    done = input("Enter done or not (yes/no): ")

    tasks[key] = {
        "title": title,
        "priority": priority,
        "done": done.lower() == "yes"
    }

# list completed tasks
done_titles = [t["title"] for t in tasks.values() if t["done"]]

print("\nThese tasks are done:")
for i, title in enumerate(done_titles, 1):
    print(i, title)


# PRIORITY SORTING
priority_rank = {"high": 1, "medium": 2, "low": 3}

# make a list of all tasks


# Convert tasks dictionary → list
task_list = []
for key in tasks:
    task_list.append(tasks[key])

# Create paired list: [priority_number, task]
paired_list = []
for task in task_list:
    rank = priority_rank[task["priority"].lower()]
    paired_list.append([rank, task])

# Sort by the priority number
paired_list.sort()

# Extract sorted tasks
sorted_tasks = []
for pair in paired_list:
    sorted_tasks.append(pair[1])

# Print sorted tasks
print("\nTasks sorted by highest priority:")
for t in sorted_tasks:
    print(t["priority"], "-", t["title"])

