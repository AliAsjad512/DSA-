def analyze_logs(log_file):
    ip_count = {}

    # Read log file
    with open(log_file, "r") as file:
        for line in file:
            ip = line.strip()
            ip_count[ip] = ip_count.get(ip, 0) + 1

    # Detect suspicious IPs
    suspicious_ips = [ip for ip, count in ip_count.items() if count > 5]

    # Save blocked IPs
    with open("blocked_ips.txt", "w") as file:
        for ip in suspicious_ips:
            file.write(ip + "\n")

    return ip_count, suspicious_ips


# ---- Run the program ----
logs, blocked = analyze_logs("server_logs.txt")

print("Login attempts per IP:")
for ip, count in logs.items():
    print(f"{ip}: {count}")

print("\nSuspicious IPs blocked:")
print(blocked)



# Test the utilities
print("📋 File Utilities Demo")
print("="*60)
list_directory()

# Get info about current file
current_file = __file__ if '__file__' in globals() else 'test.py'
info = file_info(current_file)
print(f"\n📊 File Info for: {current_file}")
for key, value in info.items():
    print(f"{key:15}: {value}")
