from extractor import extract_text
from cleaner import clean_text
from parser import parse_cv
from scorer import score_candidate

file_path = "C:/Users/vigne/Desktop/cv screening/uploads/sample.pdf"   # put any CV here

raw_text = extract_text(file_path)
cleaned_text = clean_text(raw_text)

print("\n===== RAW TEXT =====\n")
print(raw_text)

print("\n===== CLEANED TEXT =====\n")
parsed_data = parse_cv(cleaned_text)

print("\n===== PARSED OUTPUT =====\n")
for key, value in parsed_data.items():
    print(f"\n--- {key.upper()} ---\n")
    print(value[:300])
print(cleaned_text)
score = score_candidate(cleaned_text)

print("\n===== AI EVALUATION =====\n")
print(score)