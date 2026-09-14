import joblib
import numpy as np


MODEL_FILE = "fitness_level_model.pkl"


def predict_fitness_level(workout_duration, workout_days, fitness_score):
    """
    Predict the user's fitness level using the trained
    scikit-learn Random Forest model.
    """

    model = joblib.load(MODEL_FILE)

    sample = np.array([[
        workout_duration,
        workout_days,
        fitness_score
    ]])

    prediction = model.predict(sample)[0]

    levels = {
        0: "Beginner",
        1: "Intermediate",
        2: "Advanced"
    }

    return levels.get(prediction, "Unknown")


if __name__ == "__main__":
    result = predict_fitness_level(
        workout_duration=35,
        workout_days=5,
        fitness_score=72
    )

    print("Predicted Fitness Level:", result)