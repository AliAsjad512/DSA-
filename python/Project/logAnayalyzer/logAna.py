failed_ips = {}
total = success = failed = 0

with open("access.log", "r") as file:
    for line in file:
        total += 1
        ip, status = line.split()

        if status == "SUCCESS":
            success += 1
        else:
            failed += 1
            failed_ips[ip] = failed_ips.get(ip, 0) + 1

print("Total attempts:", total)
print("Successful:", success)
print("Failed:", failed)

print("Suspicious IPs:")
for ip, count in failed_ips.items():
    if count > 1:
        print(ip)



        from collections import Counter
import re

def scan_ips(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    ip_list = []
    for line in lines:
        # Extract IP using regex
        match = re.match(r"(\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ip_list.append(match.group(1))

    ip_count = Counter(ip_list)

    print("All unique IPs:")
    for ip in ip_count:
        print(f"{ip}: {ip_count[ip]} times")

    print("\nSuspicious IPs (more than 1 access):")
    for ip, count in ip_count.items():
        if count > 1:
            print(f"{ip}: {count} times")

# Example usage:
scan_ips("access.log")


