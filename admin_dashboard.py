import streamlit as st
import pandas as pd
import plotly.express as px


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
# DEMO FITNESS DATA
# ==========================================

data = pd.DataFrame({
    "User": [
        "User 1",
        "User 2",
        "User 3",
        "User 4",
        "User 5",
        "User 6",
        "User 7",
        "User 8"
    ],
    "Workout Days": [5, 4, 6, 3, 5, 2, 6, 4],
    "Missed Days": [2, 3, 1, 4, 2, 5, 1, 3],
    "Performance Score": [85, 72, 91, 65, 88, 58, 94, 76],
    "BMI": [23.4, 26.1, 22.8, 28.3, 24.5, 30.1, 21.9, 25.7],
    "Goal": [
        "Weight Loss",
        "Muscle Gain",
        "Maintain Fitness",
        "Weight Loss",
        "Muscle Gain",
        "Weight Loss",
        "Muscle Gain",
        "Maintain Fitness"
    ]
})


# ==========================================
# CALCULATE CONSISTENCY
# ==========================================

data["Consistency"] = (
    data["Workout Days"] /
    (data["Workout Days"] + data["Missed Days"])
) * 100

data["Consistency"] = data["Consistency"].round(1)


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