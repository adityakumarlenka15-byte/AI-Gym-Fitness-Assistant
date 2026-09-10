def gym_buddy(message):
    """Simple rule-based virtual gym buddy."""

    message = message.lower().strip()

    if any(word in message for word in ["motivat", "tired", "lazy", "don't feel"]):
        return (
            "Don't give up! 💪 Start with just 10 minutes. "
            "Small steps today can build a strong fitness habit."
        )

    elif any(word in message for word in ["completed", "finished", "done"]):
        return (
            "Great job! 🎉 You completed your workout. "
            "Stay consistent and remember to recover properly."
        )

    elif any(word in message for word in ["missed", "skip", "skipped"]):
        return (
            "That's okay! 👍 One missed workout doesn't ruin your progress. "
            "Get back to your routine with your next session."
        )

    elif any(word in message for word in ["workout", "exercise", "training"]):
        return (
            "Try a balanced workout with warm-up, strength exercises, "
            "some cardio, and a cool-down."
        )

    elif any(word in message for word in ["tip", "advice"]):
        return (
            "Fitness tip 💡: Focus on consistency, good exercise form, "
            "proper rest, hydration, and balanced nutrition."
        )

    elif any(word in message for word in ["hello", "hi", "hey"]):
        return (
            "Hey! 👋 I'm your Virtual Gym Buddy. "
            "How can I help you with your fitness routine today?"
        )

    else:
        return (
            "I'm here to support your fitness journey! 💪 "
            "Ask me about workouts, motivation, fitness tips, "
            "or tell me about your workout."
        )


if __name__ == "__main__":

    print("🤖 Virtual Gym Buddy")
    print("-------------------------")
    print("Type 'exit' to stop.\n")

    while True:

        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Gym Buddy: Keep going! See you next workout! 💪")
            break

        response = gym_buddy(user_message)

        print("Gym Buddy:", response)