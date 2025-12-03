tasks = {}
n = int(input("Enter the number of entries: "))

for _ in range(n):
    key = input("Enter key: ")
    title = input("Enter title: ")
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
task_list = list(tasks.values())

# sort tasks by priority
sorted_tasks = sorted(
    task_list,
    key=lambda t: priority_rank[t["priority"].lower()]
)

print("\nTasks sorted by highest priority:")
for t in sorted_tasks:
    print(f"{t['priority']} - {t['title']}")
