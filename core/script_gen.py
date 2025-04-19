# core/script_gen.py
import os
import random
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def load_gemini_api_key():
    return os.getenv("GEMINI_API_KEY")

def generate_script_with_gpt(topic: str, temperature=0.7) -> str:
    api_key = load_gemini_api_key()
    if not api_key:
        raise Exception("Gemini API key not found in environment variables.")
    
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-pro",  # ✅ correct full model path
    )

    prompt = f"""
    Write a short, engaging 60-second YouTube Shorts script about: {topic}
    - Use a fun and punchy tone
    - Hook the viewer in the first sentence
    - Write it like a voiceover script
    - Use short, engaging sentences
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Error generating script: {str(e)}]"

def generate_random_script(topic: str) -> str:
    lines = [
        f"Here's a fun fact about {topic}!",
        f"Did you know that {topic} has changed the world in many ways?",
        f"Let's break down {topic} in under 60 seconds!",
        f"{topic} might sound boring, but it's actually pretty wild when you dig deeper.",
        f"Ready to learn something cool about {topic}? Let's go!"
    ]
    return random.choice(lines) + "\n\nThis is a placeholder script while we test."
