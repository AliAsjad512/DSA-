from datetime import datetime

login_attempts = [
    {"user": "ali", "success": False, "time": "22:30"},
    {"user": "ali", "success": False, "time": "22:35"},
    {"user": "ali", "success": False, "time": "22:40"},
    {"user": "sara", "success": True,  "time": "14:10"},
    {"user": "john", "success": True,  "time": "02:15"}
]

def is_suspicious_time(time_str):
    hour = int(time_str.split(":")[0])
    return hour < 6 or hour > 22

def detect_suspicious_logins(attempts):
    failed_count = {}

    for attempt in attempts:
        user = attempt["user"]

        if not attempt["success"]:
            failed_count[user] = failed_count.get(user, 0) + 1

        if failed_count.get(user, 0) >= 3 or is_suspicious_time(attempt["time"]):
            print(f"⚠️ Suspicious activity detected for user: {user}")

# ---- Run ----
detect_suspicious_logins(login_attempts)
