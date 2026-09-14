import torch
import numpy as np
from pytorch_model import FitnessNet


MODEL_FILE = "pytorch_fitness_model.pth"


def predict_fitness_level(workout_duration, workout_days, fitness_score):

    model = FitnessNet()

    model.load_state_dict(
        torch.load(
            MODEL_FILE,
            map_location=torch.device("cpu")
        )
    )

    model.eval()

    sample = np.array(
        [[workout_duration, workout_days, fitness_score]],
        dtype=np.float32
    )

    sample_tensor = torch.tensor(sample)

    with torch.no_grad():

        output = model(sample_tensor)

        prediction = torch.argmax(
            output,
            dim=1
        ).item()

    levels = {
        0: "Beginner",
        1: "Intermediate",
        2: "Advanced"
    }

    return levels.get(
        prediction,
        "Unknown"
    )


if __name__ == "__main__":

    result = predict_fitness_level(
        workout_duration=35,
        workout_days=5,
        fitness_score=72
    )

    print("PyTorch Predicted Fitness Level:", result)