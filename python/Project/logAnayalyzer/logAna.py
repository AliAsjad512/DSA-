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

