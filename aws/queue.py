# aws/queue.py

# aws/queue.py

import os

QUEUE_FILE = "queue.txt"

def send_to_queue(file_name):
    with open(QUEUE_FILE, "a") as f:
        f.write(file_name + "\n")

def receive_message():
    if not os.path.exists(QUEUE_FILE):
        return None

    with open(QUEUE_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        return None

    first = lines[0].strip()

    with open(QUEUE_FILE, "w") as f:
        f.writelines(lines[1:])

    return first