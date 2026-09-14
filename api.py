from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import subprocess
import sys
import os

from diet_coach import diet_coach
from habit_tracker import habit_tracker
from gym_recommender import recommend_gyms, create_weekly_plan
from smart_gym_assistant import smart_gym_assistant
from gym_buddy import gym_buddy
from performance import analyze_performance
from fitness_predictor import predict_fitness_level
from pytorch_predictor import predict_fitness_level as pytorch_predict_fitness_level


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="AI Gym & Fitness Assistant API",
    description="Backend API for the AI Gym & Fitness Assistant",
    version="1.0.0"
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:5175",
        "http://127.0.0.1:5175"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# REQUEST MODELS
# =========================================================

class DietRequest(BaseModel):
    weight: float
    height: float
    age: int
    goal: str


class HabitRequest(BaseModel):
    workout_days: int
    missed_days: int


class GymRequest(BaseModel):
    goal: str
    experience: str


class GymBuddyRequest(BaseModel):
    message: str


class PerformanceRequest(BaseModel):
    form_score: float
    rep_quality: float
    consistency: float


class FitnessPredictionRequest(BaseModel):
    workout_duration: float
    workout_days: int
    fitness_score: float


class PyTorchFitnessPredictionRequest(BaseModel):
    workout_duration: float
    workout_days: int
    fitness_score: float


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():
    return {
        "message": "AI Gym & Fitness Assistant API is running",
        "status": "success"
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# =========================================================
# AI DIETICIAN
# =========================================================

@app.post("/diet")
def diet_recommendation(request: DietRequest):

    if request.goal == "Weight Loss":
        diet_goal = "Weight Loss"

    elif request.goal == "Weight Gain":
        diet_goal = "Weight Gain"

    elif request.goal == "Muscle Gain":
        diet_goal = "Weight Gain"

    else:
        diet_goal = "Maintain Weight"

    result = diet_coach(
        weight=request.weight,
        height=request.height,
        age=request.age,
        goal=diet_goal
    )

    return result


# =========================================================
# HABIT TRACKER
# =========================================================

@app.post("/habit")
def habit_analysis(request: HabitRequest):

    result = habit_tracker(
        workout_days=request.workout_days,
        missed_days=request.missed_days
    )

    return result


# =========================================================
# GYM PLANNER
# =========================================================

@app.post("/gym-recommendation")
def gym_recommendation(request: GymRequest):

    recommendations = recommend_gyms(
        goal=request.goal,
        experience=request.experience
    )

    weekly_plan = create_weekly_plan(
        request.goal
    )

    return {
        "recommendations": recommendations,
        "weekly_plan": weekly_plan
    }


# =========================================================
# SMART GYM
# =========================================================

@app.post("/smart-gym")
def smart_gym(request: GymRequest):

    result = smart_gym_assistant(
        goal=request.goal,
        experience=request.experience
    )

    return result


# =========================================================
# VIRTUAL GYM BUDDY
# =========================================================

@app.post("/gym-buddy")
def gym_buddy_chat(request: GymBuddyRequest):

    response = gym_buddy(
        request.message
    )

    return {
        "response": response
    }

@app.post("/performance")
def performance_analysis(request: PerformanceRequest):
    result = analyze_performance(
        form_score=request.form_score,
        rep_quality=request.rep_quality,
        consistency=request.consistency
    )

    return result

# =========================================================
# AI GYM TRAINER
# =========================================================

@app.post("/start-trainer")
def start_trainer():

    trainer_path = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        "workout_trainer.py"
    )

    subprocess.Popen(
        [
            sys.executable,
            trainer_path
        ],
        cwd=os.path.dirname(trainer_path)
    )

    return {
        "status": "success",
        "message": "AI Gym Trainer started"
    }

@app.post("/fitness-prediction")
def fitness_prediction(request: FitnessPredictionRequest):
    level = predict_fitness_level(
        workout_duration=request.workout_duration,
        workout_days=request.workout_days,
        fitness_score=request.fitness_score
    )

    return {
        "Predicted Fitness Level": level
    }

@app.post("/pytorch-fitness-prediction")
def pytorch_fitness_prediction(request: PyTorchFitnessPredictionRequest):

    level = pytorch_predict_fitness_level(
        workout_duration=request.workout_duration,
        workout_days=request.workout_days,
        fitness_score=request.fitness_score
    )

    return {
        "Predicted Fitness Level": level,
        "Model": "PyTorch Neural Network"
    }