import streamlit as st
import pandas as pd
import plotly.express as px
import subprocess
import sys

from diet_coach import diet_coach
from habit_tracker import habit_tracker, predict_next_workout
from gym_buddy import gym_buddy
from performance import analyze_performance
from gym_recommender import recommend_gyms, create_weekly_plan
from smart_gym_assistant import smart_gym_assistant

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Gym & Fitness Assistant",
    page_icon="🏋️",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }

    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #1e3a8a;
    }

    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #475569;
        margin-bottom: 30px;
    }

    .card {
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="title">🏋️ AI Gym & Fitness Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your AI-powered personal fitness ecosystem</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("⚙️ User Profile")

name = st.sidebar.text_input("Your Name", "User")

age = st.sidebar.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=20
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=200.0,
    value=65.0
)

height = st.sidebar.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=220.0,
    value=170.0
)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    [
        "Weight Loss",
        "Muscle Gain",
        "Maintain Fitness",
        "Improve Endurance"
    ]
)

# -----------------------------
# BMI Calculation
# -----------------------------
height_m = height / 100
bmi = weight / (height_m ** 2)

if bmi < 18.5:
    bmi_status = "Underweight"
elif bmi < 25:
    bmi_status = "Normal"
elif bmi < 30:
    bmi_status = "Overweight"
else:
    bmi_status = "Obese"

# -----------------------------
# Dashboard Metrics
# -----------------------------
st.subheader(f"👋 Welcome, {name}!")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("BMI", f"{bmi:.1f}")

with col2:
    st.metric("BMI Status", bmi_status)

with col3:
    st.metric("Weight", f"{weight:.1f} kg")

with col4:
    st.metric("Goal", goal)

# -----------------------------
# Main Modules
# -----------------------------
st.markdown("---")
st.header("🤖 AI Fitness Modules")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🏋️ AI Gym Trainer</h3>
        <p>Detect exercises, count repetitions and provide workout feedback.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🥗 AI Diet Coach</h3>
        <p>Get personalized diet suggestions based on your fitness goals.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Habit Tracker</h3>
        <p>Track workouts and analyze your fitness consistency.</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>💬 Virtual Gym Buddy</h3>
        <p>Chat with an AI fitness companion for motivation and guidance.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🎯 Performance Analyzer</h3>
        <p>Analyze workout performance and generate performance scores.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>🏢 Gym Planner</h3>
        <p>Plan workouts and discover suitable fitness programs.</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Workout Progress
# -----------------------------
st.markdown("---")
st.header("📈 Weekly Workout Progress")

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

workouts = [30, 45, 0, 40, 50, 35, 20]

df = pd.DataFrame({
    "Day": days,
    "Workout Minutes": workouts
})

fig = px.bar(
    df,
    x="Day",
    y="Workout Minutes",
    title="Weekly Workout Activity"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Fitness Recommendation
# -----------------------------
st.markdown("---")
st.header("💡 AI Fitness Recommendation")

if goal == "Weight Loss":
    recommendation = (
        "Focus on regular cardio, strength training and a balanced calorie-controlled diet."
    )

elif goal == "Muscle Gain":
    recommendation = (
        "Focus on progressive strength training, adequate protein and sufficient recovery."
    )

elif goal == "Improve Endurance":
    recommendation = (
        "Gradually increase cardio duration and include endurance-based workouts."
    )

else:
    recommendation = (
        "Maintain a balanced combination of strength training, cardio and recovery."
    )

st.info(recommendation)

# ==============================
# AI DIET COACH
# ==============================

st.markdown("---")
st.header("🥗 AI Diet Coach")

# Map dashboard goals to Diet Coach goals
if goal == "Weight Loss":
    diet_goal = "Weight Loss"

elif goal == "Muscle Gain":
    diet_goal = "Weight Gain"

else:
    diet_goal = "Maintain Weight"

diet_result = diet_coach(
    weight=weight,
    height=height,
    age=age,
    goal=diet_goal
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "BMI",
        diet_result["BMI"]
    )

with col2:
    st.metric(
        "Daily Calorie Suggestion",
        diet_result["Daily Calorie Suggestion"]
    )

st.subheader("🍽️ Meal Suggestions")

for meal, suggestion in diet_result["Meals"].items():
    st.write(f"**{meal}:** {suggestion}")

st.info(
    "💡 These are general wellness suggestions. "
    "For medical or personalized nutrition advice, consult a qualified professional."
)

# ==============================
# AI FITNESS HABIT TRACKER
# ==============================

st.markdown("---")
st.header("📅 AI Fitness Habit Tracker")

habit_col1, habit_col2 = st.columns(2)

with habit_col1:
    workout_days = st.number_input(
        "Workout Days This Week",
        min_value=0,
        max_value=7,
        value=5
    )

with habit_col2:
    missed_days = st.number_input(
        "Missed Workout Days",
        min_value=0,
        max_value=7,
        value=2
    )

habit_result = habit_tracker(
    workout_days=workout_days,
    missed_days=missed_days
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Workout Days",
        habit_result["Workout Days"]
    )

with col2:
    st.metric(
        "Missed Days",
        habit_result["Missed Days"]
    )

with col3:
    st.metric(
        "Consistency",
        f'{habit_result["Consistency"]}%'
    )

st.success(
    f'💪 {habit_result["Status"]}'
)

st.info(
    "📅 Complete your workouts consistently and maintain "
    "adequate rest and recovery."
)

# ==============================
# VIRTUAL GYM BUDDY
# ==============================

st.markdown("---")
st.header("💬 Virtual Gym Buddy")

st.write(
    "Chat with your virtual fitness companion for motivation, "
    "workout tips and encouragement."
)

user_message = st.text_input(
    "Ask your Gym Buddy:",
    placeholder="Example: I don't feel motivated today"
)

if user_message:
    response = gym_buddy(user_message)

    st.chat_message("user").write(user_message)
    st.chat_message("assistant").write(response)

# ==============================
# POSE-TO-PERFORMANCE ANALYZER
# ==============================

st.markdown("---")
st.header("🎯 Pose-to-Performance Analyzer")

st.write(
    "Evaluate your workout performance using form, "
    "rep quality and movement consistency."
)

perf_col1, perf_col2, perf_col3 = st.columns(3)

with perf_col1:
    form_score = st.slider(
        "Form Score",
        min_value=0,
        max_value=100,
        value=85
    )

with perf_col2:
    rep_quality = st.slider(
        "Rep Quality",
        min_value=0,
        max_value=100,
        value=80
    )

with perf_col3:
    consistency = st.slider(
        "Movement Consistency",
        min_value=0,
        max_value=100,
        value=90
    )

performance_result = analyze_performance(
    form_score=form_score,
    rep_quality=rep_quality,
    consistency=consistency
)

score_col1, score_col2 = st.columns(2)

with score_col1:
    st.metric(
        "Performance Score",
        performance_result["Performance Score"]
    )

with score_col2:
    st.metric(
        "Performance Level",
        performance_result["Performance Level"]
    )

st.subheader("💡 Performance Feedback")

for feedback in performance_result["Feedback"]:
    st.write("•", feedback)

# ==============================
# GYM RECOMMENDER & PLANNER
# ==============================

st.markdown("---")
st.header("🏢 Gym Recommender & Planner")

st.write(
    "Get fitness program recommendations and a simple weekly "
    "workout plan based on your fitness goal."
)

experience = st.selectbox(
    "Fitness Experience",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

# Map dashboard goals to recommender goals
if goal == "Weight Loss":
    planner_goal = "Weight Loss"

elif goal == "Muscle Gain":
    planner_goal = "Muscle Building"

elif goal == "Improve Endurance":
    planner_goal = "General Fitness"

else:
    planner_goal = "General Fitness"

recommendations = recommend_gyms(
    planner_goal,
    experience
)

st.subheader("🏋️ Recommended Programs")

for recommendation in recommendations:
    st.write("•", recommendation)

st.subheader("📅 Weekly Fitness Plan")

weekly_plan = create_weekly_plan(planner_goal)

for day in weekly_plan:
    st.write("•", day)

# ==============================
# SMART GYM ASSISTANT
# ==============================

st.markdown("---")
st.header("🤖 Smart Gym Assistant")

st.write(
    "Get AI-based workout intensity, resistance and rest-time "
    "recommendations based on your fitness goal and experience."
)

smart_result = smart_gym_assistant(
    goal=planner_goal,
    experience=experience
)

st.subheader("⚙️ Recommended Workout Settings")

settings = smart_result["Settings"]

setting_col1, setting_col2, setting_col3 = st.columns(3)

with setting_col1:
    st.metric(
        "Workout Intensity",
        settings["Workout Intensity"]
    )

with setting_col2:
    st.metric(
        "Recommended Resistance",
        settings["Recommended Resistance"]
    )

with setting_col3:
    st.metric(
        "Rest Time",
        f'{settings["Rest Time"]} seconds'
    )

st.subheader("🏋️ Equipment Status")

equipment = smart_result["Equipment"]

for item, status in equipment.items():
    if status == "Available":
        st.success(f"✅ {item}: {status}")
    else:
        st.warning(f"⚠️ {item}: {status}")
        
st.subheader("📡 Live IoT Equipment Data")

live_data = smart_result.get("Live Sensor Data", {})

if live_data.get("Live Status") == "Sensor data received":
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Equipment", live_data.get("Equipment", "Unknown"))

    with col2:
        st.metric("Heart Rate", f"{live_data.get('Heart Rate', 0)} BPM")

    with col3:
        st.metric("Resistance", live_data.get("Resistance", 0))

    with col4:
        st.metric("Intensity", live_data.get("Sensor Intensity", "Unknown"))

    st.info(
        f"💡 **Smart Recommendation:** "
        f"{live_data.get('Recommendation', 'No recommendation available.')}"
    )
else:
    st.warning(
        "No live MQTT sensor data received. "
        "Make sure the MQTT simulator is running."
    )            

# ==============================
# AI GYM TRAINER
# ==============================

st.markdown("---")
st.header("🏋️ AI Gym Trainer")

st.write(
    "Use your webcam to detect squats, count repetitions "
    "and receive real-time form feedback."
)

if st.button("▶️ Start AI Gym Trainer"):

    st.info(
        "The AI Gym Trainer will open in a separate webcam window. "
        "Press Q in the webcam window to stop the workout."
    )

    subprocess.Popen(
        [sys.executable, "workout_trainer.py"]
    )

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.caption(
    "AI Gym & Fitness Assistant | AI-powered fitness management system"
)