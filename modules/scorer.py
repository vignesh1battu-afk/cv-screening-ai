from openai import OpenAI

client = OpenAI()

def score_candidate(cv_text):

    prompt = f"""
    You are an AI CV screening assistant.

    Evaluate the candidate on:
    1. Technical Fundamentals
    2. AI Curiosity
    3. Ownership Mindset

    Give score from 0 to 10.

    Return ONLY JSON format:

    {{
        "technical_score": number,
        "ai_curiosity_score": number,
        "ownership_mindset": number,
        "overall_score": number,
        "recommendation": "Shortlist or Reject"
    }}

    CV:
    {cv_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content