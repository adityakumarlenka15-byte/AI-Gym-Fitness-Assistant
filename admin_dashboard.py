import streamlit as st
import pandas as pd
import plotly.express as px

from database import (
    users_collection,
    workouts_collection,
    habit_collection,
    performance_collection,
    diet_collection,
    iot_collection
)

# ==========================================
# ADMIN DASHBOARD
# ==========================================

st.set_page_config(
    page_title="Fitness Admin Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Gym & Fitness Assistant - Admin Dashboard")
st.write(
    "Analytics dashboard for monitoring fitness activity, "
    "performance, habits and application modules."
)

st.divider()


# ==========================================
# LOAD FITNESS DATA FROM MONGODB
# ==========================================

users = list(users_collection.find())
workouts = list(workouts_collection.find())
habits = list(habit_collection.find())
performances = list(performance_collection.find())
diet_records = list(diet_collection.find())
iot_records = list(iot_collection.find())


# ==========================================
# PREPARE USER ANALYTICS DATA
# ==========================================

user_rows = []

for user in users:

    user_id = user.get("_id")

    user_name = user.get("name", "User")
    user_goal = user.get("goal", "Maintain Fitness")

    # -----------------------------
    # Find this user's workouts
    # -----------------------------

    user_workouts = [
        workout for workout in workouts
        if workout.get("user_id") == user_id
    ]

    total_reps = 0

    for workout in user_workouts:
        reps = workout.get("reps", 0)

        try:
            total_reps += float(reps)
        except (TypeError, ValueError):
            pass

    # -----------------------------
    # Find this user's habit records
    # -----------------------------

    user_habits = [
        habit for habit in habits
        if habit.get("user_id") == user_id
    ]

    workout_days = 0
    missed_days = 0

    for habit in user_habits:
        try:
            workout_days += float(habit.get("workout_days", 0))
        except (TypeError, ValueError):
            pass

        try:
            missed_days += float(habit.get("missed_days", 0))
        except (TypeError, ValueError):
            pass

    # -----------------------------
    # Find this user's performance
    # -----------------------------

    user_performances = [
        performance for performance in performances
        if performance.get("user_id") == user_id
    ]

    performance_scores = []

    for performance in user_performances:
        try:
            performance_scores.append(
                float(performance.get("performance_score", 0))
            )
        except (TypeError, ValueError):
            pass

    if performance_scores:
        average_performance = sum(performance_scores) / len(
            performance_scores
        )
    else:
        average_performance = 0

    # -----------------------------
    # Find this user's diet records
    # -----------------------------

    user_diets = [
        diet for diet in diet_records
        if diet.get("user_id") == user_id
    ]

    bmi_values = []

    for diet in user_diets:
        try:
            bmi_values.append(
                float(diet.get("bmi", 0))
            )
        except (TypeError, ValueError):
            pass

    if bmi_values:
        average_bmi = sum(bmi_values) / len(bmi_values)
    else:
        average_bmi = 0

    # -----------------------------
    # Calculate consistency
    # -----------------------------

    total_days = workout_days + missed_days

    if total_days > 0:
        consistency = (
            workout_days / total_days
        ) * 100
    else:
        consistency = 0

    # -----------------------------
    # Add user row
    # -----------------------------

    user_rows.append({
        "User": user_name,
        "Goal": user_goal,
        "Workout Days": workout_days,
        "Missed Days": missed_days,
        "Total Reps": total_reps,
        "Performance Score": round(
            average_performance, 1
        ),
        "BMI": round(
            average_bmi, 1
        ),
        "Consistency": round(
            consistency, 1
        )
    })


# Convert user analytics to DataFrame

data = pd.DataFrame(user_rows)


# Empty database protection

if data.empty:
    data = pd.DataFrame(
        columns=[
            "User",
            "Goal",
            "Workout Days",
            "Missed Days",
            "Total Reps",
            "Performance Score",
            "BMI",
            "Consistency"
        ]
    )


# Make sure numeric columns are numeric

numeric_columns = [
    "Workout Days",
    "Missed Days",
    "Total Reps",
    "Performance Score",
    "BMI",
    "Consistency"
]

for column in numeric_columns:
    data[column] = pd.to_numeric(
        data[column],
        errors="coerce"
    ).fillna(0)

# ==========================================
# SIDEBAR FILTER
# ==========================================

st.sidebar.header("Dashboard Filters")

goal_filter = st.sidebar.selectbox(
    "Fitness Goal",
    [
        "All",
        "Weight Loss",
        "Muscle Gain",
        "Maintain Fitness"
    ]
)

if goal_filter != "All":
    filtered_data = data[data["Goal"] == goal_filter]
else:
    filtered_data = data


# ==========================================
# KEY METRICS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Users",
        len(filtered_data)
    )

with col2:
    st.metric(
        "Average Performance",
        f"{filtered_data['Performance Score'].mean():.1f}"
    )

with col3:
    st.metric(
        "Average Consistency",
        f"{filtered_data['Consistency'].mean():.1f}%"
    )

with col4:
    st.metric(
        "Average BMI",
        f"{filtered_data['BMI'].mean():.1f}"
    )


st.divider()


# ==========================================
# PERFORMANCE ANALYTICS
# ==========================================

st.header("📈 Performance Analytics")

performance_chart = px.bar(
    filtered_data,
    x="User",
    y="Performance Score",
    title="User Performance Scores"
)

st.plotly_chart(
    performance_chart,
    use_container_width=True
)


# ==========================================
# HABIT ANALYTICS
# ==========================================

st.header("📅 Fitness Habit Analytics")

habit_chart = px.bar(
    filtered_data,
    x="User",
    y=["Workout Days", "Missed Days"],
    title="Workout vs Missed Days",
    barmode="group"
)

st.plotly_chart(
    habit_chart,
    use_container_width=True
)


# ==========================================
# GOAL DISTRIBUTION
# ==========================================

st.header("🎯 Fitness Goal Distribution")

goal_counts = filtered_data["Goal"].value_counts().reset_index()
goal_counts.columns = ["Goal", "Users"]

goal_chart = px.pie(
    goal_counts,
    names="Goal",
    values="Users",
    title="Users by Fitness Goal"
)

st.plotly_chart(
    goal_chart,
    use_container_width=True
)


# ==========================================
# BMI ANALYTICS
# ==========================================

st.header("⚖️ BMI Analytics")

bmi_chart = px.scatter(
    filtered_data,
    x="BMI",
    y="Performance Score",
    size="Workout Days",
    hover_name="User",
    title="BMI vs Performance Score"
)

st.plotly_chart(
    bmi_chart,
    use_container_width=True
)

# ==============================
# IoT SENSOR ANALYTICS
# ==============================

st.markdown("---")
st.header("📡 IoT Sensor Analytics")

if iot_records:
    heart_rates = []
    resistances = []
    equipment_names = []

    for record in iot_records:
        try:
            heart_rates.append(float(record.get("heart_rate", 0)))
        except (TypeError, ValueError):
            pass

        try:
            resistances.append(float(record.get("resistance", 0)))
        except (TypeError, ValueError):
            pass

        equipment = record.get("equipment")
        if equipment:
            equipment_names.append(equipment)

    average_heart_rate = (
        sum(heart_rates) / len(heart_rates)
        if heart_rates else 0
    )

    average_resistance = (
        sum(resistances) / len(resistances)
        if resistances else 0
    )

    iot_col1, iot_col2, iot_col3 = st.columns(3)

    with iot_col1:
        st.metric(
            "IoT Sensor Records",
            len(iot_records)
        )

    with iot_col2:
        st.metric(
            "Average Heart Rate",
            f"{average_heart_rate:.1f} BPM"
        )

    with iot_col3:
        st.metric(
            "Average Resistance",
            f"{average_resistance:.1f}"
        )

    if equipment_names:
        equipment_df = pd.DataFrame({
            "Equipment": equipment_names
        })

        equipment_counts = (
            equipment_df["Equipment"]
            .value_counts()
            .reset_index()
        )

        equipment_counts.columns = [
            "Equipment",
            "Records"
        ]

        fig_iot = px.bar(
            equipment_counts,
            x="Equipment",
            y="Records",
            title="IoT Equipment Usage"
        )

        st.plotly_chart(
            fig_iot,
            use_container_width=True
        )

else:
    st.info(
        "No IoT sensor records available yet. "
        "Run the MQTT sensor simulator to collect data."
    )

# ==========================================
# MODULE STATUS
# ==========================================

st.header("🧩 System Module Status")

module_status = pd.DataFrame({
    "Module": [
        "AI Gym Trainer",
        "AI Diet Coach",
        "Fitness Habit Tracker",
        "Virtual Gym Buddy",
        "Performance Analyzer",
        "Gym Recommender & Planner",
        "Smart Gym Assistant",
        "FastAPI Backend"
    ],
    "Status": [
        "Working",
        "Working",
        "Working",
        "Working",
        "Working",
        "Working",
        "Working",
        "Working"
    ]
})

st.dataframe(
    module_status,
    use_container_width=True,
    hide_index=True
)


# ==========================================
# USER DATA TABLE
# ==========================================

st.header("👥 Fitness User Analytics")

st.dataframe(
    filtered_data,
    use_container_width=True,
    hide_index=True
)


st.divider()

st.caption(
    "AI Gym & Fitness Assistant | Admin Analytics Dashboard"
)
