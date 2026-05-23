from app.core.config import OPENAI_API_KEY


def generate_answer(question: str, context: str) -> str:
    if not OPENAI_API_KEY:
        return (
            "OPENAI_API_KEY is missing. Retrieved context:\n\n"
            + context
        )

    from openai import OpenAI

    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
You are a healthcare information assistant.

Rules:
- Use only the given context.
- Do not diagnose.
- Do not prescribe medication.
- Do not replace professional medical advice.
- If the answer is not in the context, say you do not have enough information.

Question:
{question}

Context:
{context}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You provide safe, grounded healthcare information."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content