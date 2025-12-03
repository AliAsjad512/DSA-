priority_rank = {"high": 1, "medium": 2, "low": 3}

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
