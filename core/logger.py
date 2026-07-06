from datetime import datetime

LOG_FILE = "logs/sepehr.log"


def log(message):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")
