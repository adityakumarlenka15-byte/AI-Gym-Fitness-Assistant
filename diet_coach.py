def calculate_bmi(weight, height):
    """Calculate BMI from weight (kg) and height (cm)."""
    height_m = height / 100

    if height_m <= 0:
        return 0

    return weight / (height_m ** 2)


def get_calorie_suggestion(weight, height, age, goal):
    """Give a simple general calorie suggestion."""

    bmi = calculate_bmi(weight, height)

    # Simple estimated maintenance calories
    maintenance = (10 * weight) + (6.25 * height) - (5 * age) + 5

    if goal == "Weight Loss":
        calories = maintenance - 300
    elif goal == "Weight Gain":
        calories = maintenance + 300
    else:
        calories = maintenance

    return round(bmi, 1), round(calories)


def get_meal_suggestions(goal):
    """Return general healthy meal suggestions."""

    meals = {
        "Weight Loss": {
            "Breakfast": "Oats, fruits, eggs or low-fat yogurt",
            "Lunch": "Brown rice/roti, vegetables, dal and a protein source",
            "Snack": "Fruits, nuts or yogurt",
            "Dinner": "Vegetables, roti and a lean protein source"
        },

        "Weight Gain": {
            "Breakfast": "Oats, banana, milk, eggs and nuts",
            "Lunch": "Rice/roti, vegetables, dal, paneer/chicken and yogurt",
            "Snack": "Banana shake, nuts or peanut butter sandwich",
            "Dinner": "Rice/roti, vegetables and a protein-rich food"
        },

        "Maintain Weight": {
            "Breakfast": "Oats, fruits, eggs or yogurt",
            "Lunch": "Rice/roti, vegetables, dal and protein",
            "Snack": "Fruits and a small portion of nuts",
            "Dinner": "Balanced vegetables, carbohydrates and protein"
        }
    }

    return meals.get(goal, meals["Maintain Weight"])


def diet_coach(weight, height, age, goal):
    """Generate a simple diet-coach result."""

    bmi, calories = get_calorie_suggestion(
        weight,
        height,
        age,
        goal
    )

    meals = get_meal_suggestions(goal)

    return {
        "BMI": bmi,
        "Daily Calorie Suggestion": calories,
        "Meals": meals
    }


if __name__ == "__main__":

    result = diet_coach(
        weight=70,
        height=170,
        age=21,
        goal="Weight Loss"
    )

    print("AI Diet Coach")
    print("-------------------------")
    print("BMI:", result["BMI"])
    print(
        "Daily Calorie Suggestion:",
        result["Daily Calorie Suggestion"]
    )
    print()

    for meal, suggestion in result["Meals"].items():
        print(f"{meal}: {suggestion}")