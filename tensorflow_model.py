import numpy as np
import tensorflow as tf

print("TensorFlow version:", tf.__version__)

# Training data
# Features:
# [workout duration, workout days, fitness score, exercise quality]
X = np.array([
    [20, 3, 60, 65],
    [25, 3, 65, 68],
    [30, 4, 70, 72],
    [35, 4, 75, 76],
    [40, 5, 80, 82],
    [45, 5, 85, 86],
    [50, 6, 88, 90],
    [55, 6, 92, 94],
    [30, 3, 68, 70],
    [40, 4, 78, 80],
    [45, 5, 83, 85],
    [50, 5, 90, 91],
], dtype=np.float32)

# Target: workout performance score
y = np.array([
    62, 66, 71, 76, 82, 86,
    89, 94, 69, 79, 84, 91
], dtype=np.float32)

# Build TensorFlow neural network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(1)
])

# Compile model
model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

print("Training TensorFlow model...")

# Train
model.fit(
    X,
    y,
    epochs=100,
    verbose=0
)

print("Training completed successfully.")

# Save model
model.save("fitness_performance_model.keras")

print("Model saved as fitness_performance_model.keras")

# Test prediction
sample = np.array([
    [40, 5, 85, 90]
], dtype=np.float32)

prediction = model.predict(sample, verbose=0)

print(
    "Predicted Workout Performance Score:",
    round(float(prediction[0][0]), 2)
)