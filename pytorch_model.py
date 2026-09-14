import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


class FitnessNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(3, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 3)
        )

    def forward(self, x):
        return self.network(x)


def train_model():
    print("Training PyTorch fitness model...")

    X = np.array([
        [20, 3, 50],
        [25, 4, 55],
        [30, 5, 60],
        [35, 5, 72],
        [40, 6, 75],
        [45, 7, 80],
        [50, 7, 85],
        [55, 6, 88],
        [60, 7, 92],
    ], dtype=np.float32)

    y = np.array([
        0,
        0,
        0,
        1,
        1,
        1,
        2,
        2,
        2
    ], dtype=np.int64)

    X_tensor = torch.tensor(X)
    y_tensor = torch.tensor(y)

    model = FitnessNet()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    epochs = 500

    for epoch in range(epochs):

        optimizer.zero_grad()

        outputs = model(X_tensor)

        loss = criterion(outputs, y_tensor)

        loss.backward()

        optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(
                f"Epoch [{epoch + 1}/{epochs}], "
                f"Loss: {loss.item():.4f}"
            )

    torch.save(model.state_dict(), "pytorch_fitness_model.pth")

    print("\nPyTorch model trained successfully.")
    print("Model saved as pytorch_fitness_model.pth")

    # Training accuracy
    with torch.no_grad():
        outputs = model(X_tensor)
        predictions = torch.argmax(outputs, dim=1)
        accuracy = (predictions == y_tensor).float().mean()

    print(
        "Training accuracy:",
        round(accuracy.item() * 100, 2),
        "%"
    )

    # Sample prediction
    sample = torch.tensor(
        [[35, 5, 72]],
        dtype=torch.float32
    )

    with torch.no_grad():
        prediction = torch.argmax(model(sample), dim=1).item()

    levels = {
        0: "Beginner",
        1: "Intermediate",
        2: "Advanced"
    }

    print("Sample prediction:", levels[prediction])


if __name__ == "__main__":
    train_model()