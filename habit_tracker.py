from datetime import datetime, timedelta


def calculate_consistency(workout_days, total_days=7):
    """Calculate weekly workout consistency percentage."""

    if total_days <= 0:
        return 0

    return round((workout_days / total_days) * 100, 1)


def get_habit_status(consistency):
    """Return a simple habit status."""

    if consistency >= 80:
        return "Excellent consistency! Keep it up."
    elif consistency >= 60:
        return "Good consistency. Try to stay regular."
    elif consistency >= 40:
        return "You are making progress. Aim for more workout days."
    else:
        return "Try to build a regular workout routine."


def predict_next_workout(workout_dates):
    """Suggest the next workout date based on recent activity."""

    if not workout_dates:
        return datetime.now().date()

    dates = sorted(workout_dates)

    if len(dates) >= 2:
        gap = (dates[-1] - dates[-2]).days

        if gap <= 0:
            gap = 1
    else:
        gap = 1

    return dates[-1] + timedelta(days=gap)


def habit_tracker(workout_days, missed_days):
    """Generate a simple weekly habit report."""

    total_days = workout_days + missed_days

    if total_days == 0:
        total_days = 7

    consistency = calculate_consistency(
        workout_days,
        total_days
    )

    status = get_habit_status(consistency)

    return {
        "Workout Days": workout_days,
        "Missed Days": missed_days,
        "Consistency": consistency,
        "Status": status
    }


if __name__ == "__main__":

    result = habit_tracker(
        workout_days=5,
        missed_days=2
    )

    print("AI Fitness Habit Tracker")
    print("-------------------------")
    print("Workout Days:", result["Workout Days"])
    print("Missed Days:", result["Missed Days"])
    print("Consistency:", str(result["Consistency"]) + "%")
    print("Status:", result["Status"])

    workout_dates = [
        datetime(2026, 9, 7).date(),
        datetime(2026, 9, 8).date(),
        datetime(2026, 9, 10).date()
    ]

    next_workout = predict_next_workout(workout_dates)

    print("Suggested Next Workout:", next_workout)