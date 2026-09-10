# AI Gym & Fitness Assistant

## Project Overview

AI Gym & Fitness Assistant is a modular fitness application that combines workout assistance, diet guidance, habit tracking, performance analysis, gym recommendations, smart gym settings, and a virtual fitness buddy in one Streamlit dashboard.

## Features

### 1. AI Gym Trainer
- Uses OpenCV and MediaPipe for pose detection.
- Detects squat movements.
- Counts repetitions.
- Calculates knee angle.
- Provides basic workout feedback.

### 2. AI Diet Coach
- Calculates BMI.
- Provides a daily calorie suggestion.
- Generates basic meal suggestions according to the selected fitness goal.

### 3. Fitness Habit Tracker
- Tracks workout and missed days.
- Calculates consistency percentage.
- Provides habit-status feedback.
- Suggests the next workout date.

### 4. Virtual Gym Buddy
- Provides fitness motivation and guidance.
- Responds to common workout-related messages.

### 5. Performance Analyzer
- Calculates a performance score using form quality, repetition quality, and consistency.
- Provides a performance level and feedback.

### 6. Gym Recommender & Planner
- Recommends gym/program types based on fitness goal and experience.
- Generates a weekly fitness plan.

### 7. Smart Gym Assistant
- Provides workout intensity, resistance, and rest-time recommendations.
- Displays simulated gym equipment availability.

## Technology Stack

- Python
- Streamlit
- OpenCV
- MediaPipe
- Pandas
- NumPy
- Scikit-learn
- Plotly

## Project Structure

```text
AI-Gym-Fitness-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── workout_trainer.py
├── diet_coach.py
├── habit_tracker.py
├── gym_buddy.py
├── performance.py
├── gym_recommender.py
└── smart_gym_assistant.py