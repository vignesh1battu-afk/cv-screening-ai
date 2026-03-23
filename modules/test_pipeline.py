from extractor import extract_text
from cleaner import clean_text

file_path = "C:/Users/vigne/Desktop/cv screening/uploads/sample.pdf"   # put any CV here

raw_text = extract_text(file_path)
cleaned_text = clean_text(raw_text)

print("\n===== RAW TEXT =====\n")
print(raw_text)

print("\n===== CLEANED TEXT =====\n")
print(cleaned_text)