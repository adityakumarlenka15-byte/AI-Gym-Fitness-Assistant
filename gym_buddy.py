import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gemma3:1b"


def gym_buddy(message):
    """LLM-powered Virtual Gym Buddy using local Ollama."""

    prompt = f"""
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
- If the user asks about an injury or serious medical issue, recommend consulting a qualified healthcare professional.
- Do not claim to be a doctor or personal medical professional.

User message:
{message}

Respond as the Virtual Gym Buddy.
"""

    try:
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
    print("Powered by Ollama + Gemma 3:1B")
    print("Type 'exit' to stop.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Gym Buddy: Keep going! See you next workout! 💪")
            break

        response = gym_buddy(user_message)
        print("Gym Buddy:", response)