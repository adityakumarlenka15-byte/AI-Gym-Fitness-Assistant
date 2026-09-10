def calculate_performance_score(
    form_score,
    rep_quality,
    consistency
):
    """
    Calculate an overall exercise performance score.

    Each input should be between 0 and 100.
    """

    form_score = max(0, min(100, form_score))
    rep_quality = max(0, min(100, rep_quality))
    consistency = max(0, min(100, consistency))

    score = (
        (form_score * 0.40)
        + (rep_quality * 0.35)
        + (consistency * 0.25)
    )

    return round(score, 1)


def get_performance_level(score):
    """Return a performance level based on the score."""

    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Average"
    else:
        return "Needs Improvement"


def get_feedback(form_score, rep_quality, consistency):
    """Generate simple performance feedback."""

    feedback = []

    if form_score < 70:
        feedback.append(
            "Focus on improving your exercise form."
        )

    if rep_quality < 70:
        feedback.append(
            "Try to perform each repetition with controlled movement."
        )

    if consistency < 70:
        feedback.append(
            "Work on maintaining consistent movement throughout the exercise."
        )

    if not feedback:
        feedback.append(
            "Great performance! Keep maintaining your current form and consistency."
        )

    return feedback


def analyze_performance(
    form_score,
    rep_quality,
    consistency
):
    """Generate a complete performance report."""

    score = calculate_performance_score(
        form_score,
        rep_quality,
        consistency
    )

    level = get_performance_level(score)

    feedback = get_feedback(
        form_score,
        rep_quality,
        consistency
    )

    return {
        "Performance Score": score,
        "Performance Level": level,
        "Feedback": feedback
    }


if __name__ == "__main__":

    result = analyze_performance(
        form_score=85,
        rep_quality=80,
        consistency=90
    )

    print("Pose-to-Performance Analyzer")
    print("-----------------------------")

    print(
        "Performance Score:",
        result["Performance Score"]
    )

    print(
        "Performance Level:",
        result["Performance Level"]
    )

    print("\nFeedback:")

    for item in result["Feedback"]:
        print("-", item)