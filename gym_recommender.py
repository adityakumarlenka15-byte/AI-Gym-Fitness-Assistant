def recommend_gyms(goal, experience):
    """Recommend suitable gym/program types."""

    recommendations = {
        "Weight Loss": [
            "Cardio & Strength Training Gym",
            "HIIT Fitness Program",
            "Functional Training Program"
        ],
        "Weight Gain": [
            "Strength Training Gym",
            "Weightlifting Program",
            "Muscle Building Program"
        ],
        "Muscle Building": [
            "Strength & Conditioning Gym",
            "Weightlifting Program",
            "Bodybuilding Program"
        ],
        "General Fitness": [
            "Full-Body Fitness Gym",
            "Functional Training Program",
            "Group Fitness Program"
        ]
    }

    options = recommendations.get(
        goal,
        recommendations["General Fitness"]
    )

    if experience == "Beginner":
        options = [
            option + " - Beginner Friendly"
            for option in options
        ]

    return options


def create_weekly_plan(goal):
    """Create a simple weekly fitness plan."""

    plans = {
        "Weight Loss": [
            "Monday - Cardio + Core",
            "Tuesday - Full Body Strength",
            "Wednesday - Active Recovery",
            "Thursday - Cardio + Strength",
            "Friday - Full Body Workout",
            "Saturday - Light Cardio",
            "Sunday - Rest"
        ],

        "Weight Gain": [
            "Monday - Chest + Triceps",
            "Tuesday - Back + Biceps",
            "Wednesday - Rest",
            "Thursday - Legs",
            "Friday - Shoulders + Core",
            "Saturday - Full Body Strength",
            "Sunday - Rest"
        ],

        "Muscle Building": [
            "Monday - Chest + Triceps",
            "Tuesday - Back + Biceps",
            "Wednesday - Legs",
            "Thursday - Rest",
            "Friday - Shoulders + Core",
            "Saturday - Full Body Strength",
            "Sunday - Rest"
        ],

        "General Fitness": [
            "Monday - Full Body Workout",
            "Tuesday - Cardio",
            "Wednesday - Strength Training",
            "Thursday - Active Recovery",
            "Friday - Full Body Workout",
            "Saturday - Cardio + Core",
            "Sunday - Rest"
        ]
    }

    return plans.get(
        goal,
        plans["General Fitness"]
    )


if __name__ == "__main__":

    goal = "Weight Loss"
    experience = "Beginner"

    print("Gym Recommender & Planner")
    print("-------------------------")

    print("\nRecommended Programs:")

    recommendations = recommend_gyms(
        goal,
        experience
    )

    for recommendation in recommendations:
        print("-", recommendation)

    print("\nWeekly Fitness Plan:")

    weekly_plan = create_weekly_plan(goal)

    for day in weekly_plan:
        print("-", day)