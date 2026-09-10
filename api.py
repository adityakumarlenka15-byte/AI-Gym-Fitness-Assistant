from fastapi import FastAPI
from pydantic import BaseModel

from diet_coach import diet_coach
from habit_tracker import habit_tracker
from gym_recommender import recommend_gyms, create_weekly_plan
from smart_gym_assistant import smart_gym_assistant


# ==========================================
# FASTAPI BACKEND
# ==========================================

app = FastAPI(
    title="AI Gym & Fitness Assistant API",
    description="Backend API for the AI Gym & Fitness Assistant",
    version="1.0.0"
)


# ==========================================
# DATA MODELS
# ==========================================

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


# ==========================================
# HOME ENDPOINT
# ==========================================

@app.get("/")
def home():
    return {
        "message": "AI Gym & Fitness Assistant API is running",
        "status": "success"
    }


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# ==========================================
# DIET COACH API
# ==========================================

@app.post("/diet")
def diet_recommendation(request: DietRequest):

    # Map dashboard goals to Diet Coach goals
    if request.goal == "Weight Loss":
        diet_goal = "Weight Loss"

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


# ==========================================
# HABIT TRACKER API
# ==========================================

@app.post("/habit")
def habit_analysis(request: HabitRequest):

    result = habit_tracker(
        workout_days=request.workout_days,
        missed_days=request.missed_days
    )

    return result


# ==========================================
# GYM RECOMMENDER API
# ==========================================

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


# ==========================================
# SMART GYM ASSISTANT API
# ==========================================

@app.post("/smart-gym")
def smart_gym(request: GymRequest):

    result = smart_gym_assistant(
        goal=request.goal,
        experience=request.experience
    )

    return result