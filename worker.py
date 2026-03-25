# worker.py

from aws.queue import receive_message
from modules.extractor import extract_text
from modules.cleaner import clean_text
from modules.parser import parse_cv
from modules.scorer import score_candidate
import json


def process_cv(file_name):

    file_path = f"C:/Users/vigne/Desktop/cv screening/uploads/{file_name}"

    text = extract_text(file_path)
    clean = clean_text(text)
    parsed = parse_cv(clean)
    score = score_candidate(clean)

    result = {
        "file": file_name,
        "parsed": parsed,
        "score": score
    }

    with open("results/output.json", "a") as f:
        json.dump(result, f)
        f.write("\n")


def run_worker():
    print("Worker started...")

    while True:
        file_name = receive_message()

        if file_name:
            print(f"Processing: {file_name}")
            process_cv(file_name)


if __name__ == "__main__":
    run_worker()