import os
import time

LOG_DIR = "logs"
DAYS_OLD = 30
NOW = time.time()

for log_file in os.listdir(LOG_DIR):
    file_path = os.path.join(LOG_DIR, log_file)
    if os.path.isfile(file_path) and NOW - os.path.getmtime(file_path) > DAYS_OLD * 86400:
        os.remove(file_path)
        print(f"Eliminado: {log_file}")
