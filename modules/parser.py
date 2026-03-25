# modules/parser.py

def extract_section(text, section_name):
    text_lower = text.lower()

    if section_name in text_lower:
        start = text_lower.find(section_name)
        return text[start:start + 800]  
    return ""

def parse_cv(text):

    return {
        "skills": extract_section(text, "skills"),
        "projects": extract_section(text, "projects"),
        "experience": extract_section(text, "experience"),
        "education": extract_section(text, "education")
    }