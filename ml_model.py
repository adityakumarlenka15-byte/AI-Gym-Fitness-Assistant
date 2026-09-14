import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


# ---------------------------------------
# Sample workout dataset
# ---------------------------------------

X = np.array([
    [20, 5, 60],
    [25, 6, 65],
    [30, 7, 70],
    [35, 8, 75],
    [40, 9, 80],
    [45, 10, 85],
    [50, 11, 90],
    [22, 4, 55],
    [28, 5, 60],
    [32, 6, 68],
    [38, 7, 72],
    [42, 8, 78],
    [48, 9, 84],
    [55, 10, 88],
])

# Features:
# [Workout Duration (minutes),
#  Workout Days per Week,
#  Fitness Score]

# Target:
# 0 = Beginner
# 1 = Intermediate
# 2 = Advanced

y = np.array([
    0, 0, 0, 1, 1, 1, 2,
    0, 0, 1, 1, 1, 2, 2
])


# ---------------------------------------
# Split dataset
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# ---------------------------------------
# Train Random Forest model
# ---------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# ---------------------------------------
# Evaluate model
# ---------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Scikit-learn model trained successfully.")
print("Model accuracy:", round(accuracy * 100, 2), "%")


# ---------------------------------------
# Save model
# ---------------------------------------

joblib.dump(model, "fitness_level_model.pkl")

print("Model saved as fitness_level_model.pkl")


# ---------------------------------------
# Test prediction
# ---------------------------------------

sample = np.array([[35, 5, 72]])

prediction = model.predict(sample)[0]

levels = {
    0: "Beginner",
    1: "Intermediate",
    2: "Advanced"
}

print("Sample prediction:", levels[prediction])