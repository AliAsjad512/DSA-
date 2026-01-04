# Simple Log Analyzer
# Counts failed login attempts from a log file

log_data = [
    "2026-01-03 INFO User admin logged in",
    "2026-01-03 ERROR Failed login for user root",
    "2026-01-03 ERROR Failed login for user admin",
    "2026-01-03 INFO User guest logged in",
    "2026-01-03 ERROR Failed login for user root",
]

failed_attempts = {}

for line in log_data:
    if "Failed login" in line:
        user = line.split("user")[-1].strip()
        failed_attempts[user] = failed_attempts.get(user, 0) + 1

print("Failed Login Report")
print("-" * 20)

for user, count in failed_attempts.items():
    print(f"{user}: {count} failed attempts")

# Alert if brute-force suspected
for user, count in failed_attempts.items():
    if count >= 2:
        print(f"⚠️ ALERT: Possible brute-force attack on user '{user}'")
