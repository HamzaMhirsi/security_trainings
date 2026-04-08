#!/usr/bin/env python3

import json
import random
from datetime import datetime, timedelta, timezone

OUTPUT_FILE = "logs.json"
NUM_LOGS = 10000  # change this to scale

IPS = ["185.23.44.91", "192.168.1.10", "10.0.0.5", "172.16.0.3"]
PATHS = ["/login", "/admin", "/api/data", "/dashboard", "/.env"]
METHODS = ["GET", "POST"]
USER_AGENTS = ["Mozilla/5.0", "curl/7.68.0", "python-requests/2.28"]
MESSAGES = [
    "Failed login for user admin",
    "Successful login",
    "Access denied",
    "Invalid token",
]

STATUSES = [200, 401, 403, 500]

def generate_logs(n):
    logs = []
    base_time = datetime.now(timezone.utc)

    for i in range(n):
        log = {
            "timestamp": (base_time - timedelta(seconds=i)).isoformat(),
            "ip": random.choice(IPS),
            "method": random.choice(METHODS),
            "path": random.choice(PATHS),
            "status": random.choice(STATUSES),
            "user_agent": random.choice(USER_AGENTS),
            "message": random.choice(MESSAGES),
        }
        logs.append(log)

    return logs


if __name__ == "__main__":
    logs = generate_logs(NUM_LOGS)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    print(f"[+] Generated {NUM_LOGS} logs in {OUTPUT_FILE}")
