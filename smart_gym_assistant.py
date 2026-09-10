# ==========================================
# SMART GYM ASSISTANT
# ==========================================

def get_workout_settings(goal, experience):

    # Default settings
    intensity = "Moderate"
    resistance = "Medium"
    rest_time = 60

    # Goal-based settings
    if goal == "Weight Loss":
        intensity = "High"
        resistance = "Medium"
        rest_time = 45

    elif goal == "Muscle Gain":
        intensity = "High"
        resistance = "High"
        rest_time = 90

    elif goal == "Improve Endurance":
        intensity = "Moderate"
        resistance = "Low"
        rest_time = 45

    else:
        intensity = "Moderate"
        resistance = "Medium"
        rest_time = 60

    # Experience adjustment
    if experience == "Beginner":
        if intensity == "High":
            intensity = "Moderate"

        if resistance == "High":
            resistance = "Medium"

    elif experience == "Advanced":
        if intensity == "Moderate":
            intensity = "High"

    return {
        "Workout Intensity": intensity,
        "Recommended Resistance": resistance,
        "Rest Time": rest_time
    }


def get_equipment_status():

    return {
        "Treadmill": "Available",
        "Exercise Bike": "Available",
        "Weight Machine": "Available",
        "Dumbbells": "Available"
    }


def smart_gym_assistant(goal, experience):

    settings = get_workout_settings(
        goal,
        experience
    )

    equipment = get_equipment_status()

    return {
        "Settings": settings,
        "Equipment": equipment
    }


# ==========================================
# Test the Smart Gym Assistant
# ==========================================

if __name__ == "__main__":

    result = smart_gym_assistant(
        goal="Weight Loss",
        experience="Beginner"
    )

    print("🤖 Smart Gym Assistant")
    print("-------------------------")

    print("\nWorkout Settings:")

    for key, value in result["Settings"].items():
        print(f"{key}: {value}")

    print("\nEquipment Status:")

    for equipment, status in result["Equipment"].items():
        print(f"{equipment}: {status}")