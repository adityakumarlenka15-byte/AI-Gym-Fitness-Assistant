import os
import requests
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama").lower()

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gemma3:1b"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def build_prompt(message):
    return f"""
You are an AI Virtual Gym Buddy inside an AI Gym & Fitness Assistant.

Your job is to:
- motivate users during workouts
- provide general fitness guidance
- suggest safe workout habits
- give simple exercise tips
- encourage consistency, hydration and recovery

Keep responses friendly, practical and concise.

Important:
- Do not diagnose medical conditions.
- Do not provide dangerous exercise instructions.
- If the user asks about an injury or serious medical issue,
  recommend consulting a qualified healthcare professional.
- Do not claim to be a doctor or medical professional.

User message:
{message}

Respond as the Virtual Gym Buddy.
"""


def ask_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()

    return data.get(
        "response",
        "Sorry, I couldn't generate a response right now."
    ).strip()


def ask_openai(prompt):
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": OPENAI_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful and safe AI Virtual Gym Buddy."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        },
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"].strip()


def gym_buddy(message):
    """AI Virtual Gym Buddy with Ollama/OpenAI provider support."""

    prompt = build_prompt(message)

    # Use OpenAI only when explicitly configured and a key exists.
    if LLM_PROVIDER == "openai" and OPENAI_API_KEY:
        try:
            return ask_openai(prompt)

        except Exception as error:
            print("OpenAI error:", error)
            print("Falling back to Ollama...")

    # Default/local fallback
    try:
        return ask_ollama(prompt)

    except requests.exceptions.ConnectionError:
        return (
            "I couldn't connect to Ollama. "
            "Please make sure Ollama is running."
        )

    except requests.exceptions.Timeout:
        return (
            "The AI response took too long. "
            "Please try again."
        )

    except Exception as error:
        print("Gym Buddy error:", error)
        return (
            "Sorry, I couldn't generate a response right now."
        )


if __name__ == "__main__":
    print("🤖 AI Virtual Gym Buddy")
    print("-------------------------")
    print("LLM Provider:", LLM_PROVIDER)
    print("Ollama Model:", OLLAMA_MODEL)

    if LLM_PROVIDER == "openai" and OPENAI_API_KEY:
        print("External LLM: OpenAI API")
    else:
        print("External LLM: Not configured")
        print("Using local Ollama fallback.")

    print("Type 'exit' to stop.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Gym Buddy: Keep going! See you next workout! 💪")
            break

        response = gym_buddy(user_message)
        print("Gym Buddy:", response)