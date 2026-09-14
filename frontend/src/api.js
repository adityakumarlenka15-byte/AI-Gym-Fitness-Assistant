const API_URL = "http://127.0.0.1:8000";

export async function getHealth() {
  const response = await fetch(`${API_URL}/health`);

  if (!response.ok) {
    throw new Error("Backend connection failed");
  }

  return response.json();
}

export async function getDietRecommendation(data) {
  const response = await fetch(`${API_URL}/diet`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Diet API request failed");
  }

  return response.json();
}

export async function getHabitAnalysis(data) {
  const response = await fetch(`${API_URL}/habit`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Habit API request failed");
  }

  return response.json();
}

export async function getGymRecommendation(data) {
  const response = await fetch(`${API_URL}/gym-recommendation`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Gym recommendation API request failed");
  }

  return response.json();
}

export async function getSmartGym(data) {
  const response = await fetch(`${API_URL}/smart-gym`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Smart Gym API request failed");
  }

  return response.json();
}

export async function startTrainer() {
  const response = await fetch(`${API_URL}/start-trainer`, {
    method: "POST",
  });

  if (!response.ok) {
    throw new Error("Could not start AI Gym Trainer");
  }

  return response.json();
}

export async function sendGymBuddyMessage(message) {
  const response = await fetch(`${API_URL}/gym-buddy`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: message,
    }),
  });

  if (!response.ok) {
    throw new Error("Gym Buddy request failed");
  }

  return response.json();
}

export async function getPerformanceAnalysis(data) {
  const response = await fetch(`${API_URL}/performance`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Performance API request failed");
  }

  return response.json();
}

export async function getPyTorchFitnessPrediction(data) {
  const response = await fetch(
    `${API_URL}/pytorch-fitness-prediction`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }
  );

  if (!response.ok) {
    throw new Error("PyTorch fitness prediction request failed");
  }

  return response.json();
}