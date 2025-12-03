tasks = {}
n = int(input("Enter the number of entries: "))

for _ in range(n):
    key = input("Enter key: ")
    title = input("Enter title: ")
    priority = input("Enter priority: ")
    done = input("Enter done or not (yes/no): ")

    tasks[key] = {
        "title": title,
        "priority": priority,
        "done": done.lower() == "yes"  # convert to boolean
    }

# list incomplete tasks, titles only
incomplete_titles = [t["title"] for t in tasks.values() if  t["done"]]

for i, title in enumerate(incomplete_titles, 1):
    print(i, title)