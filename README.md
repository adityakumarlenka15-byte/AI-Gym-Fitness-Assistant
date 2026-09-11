# AI Gym & Fitness Assistant

AI Gym & Fitness Assistant is a modular AI-based fitness-support system developed as an academic prototype/MVP. It combines workout assistance, diet guidance, habit tracking, performance analysis, gym recommendations, smart gym settings, conversational motivation, backend APIs, and an admin analytics dashboard.

## Project Features

### 1. AI Gym Trainer
- Webcam-based workout assistance
- MediaPipe pose detection
- Squat repetition counting
- Knee-angle calculation
- Basic form feedback

### 2. AI Diet Coach
- BMI calculation
- General calorie suggestions
- Goal-based meal recommendations
- Supports Weight Loss, Muscle Gain, and Maintain Weight

### 3. Fitness Habit Tracker
- Workout-day tracking
- Missed-day tracking
- Consistency calculation
- Habit status feedback
- Next-workout prediction

### 4. Virtual Gym Buddy
- Rule-based fitness conversation
- Motivation and encouragement
- Workout guidance
- Supportive fitness responses

### 5. Performance Analyzer
- Form score
- Repetition-quality score
- Consistency score
- Overall performance score
- Performance level and feedback

### 6. Gym Recommender & Planner
- Goal-based gym/program recommendations
- Experience-based recommendations
- Weekly fitness plan generation

### 7. Smart Gym Assistant
- Workout intensity recommendation
- Resistance recommendation
- Rest-time recommendation
- Simulated gym equipment availability

### 8. FastAPI Backend

The project includes a FastAPI backend that provides an integration layer for the modular fitness services.

Available API endpoints include:

- `GET /`
- `GET /health`
- `POST /diet`
- `POST /habit`
- `POST /gym-recommendation`
- `POST /smart-gym`

FastAPI automatically provides interactive API documentation through Swagger UI.

### 9. Admin Dashboard

The project includes a separate Streamlit Admin Dashboard for analytics and monitoring.

The dashboard provides:

- Total users
- Average performance
- Average consistency
- Average BMI
- Performance analytics
- Workout vs missed-day analytics
- Fitness goal distribution
- BMI vs performance visualization
- System module status
- User fitness analytics

The current Admin Dashboard uses demonstration/sample data because a persistent database has not been implemented.

## Technology Stack

- Python
- Streamlit
- FastAPI
- Uvicorn
- OpenCV
- MediaPipe
- Pandas
- NumPy
- Plotly
- Scikit-learn

## Project Structure

```text
AI-Gym-Fitness-Assistant/
│
├── app.py
├── api.py
├── admin_dashboard.py
├── diet_coach.py
├── gym_buddy.py
├── gym_recommender.py
├── habit_tracker.py
├── performance.py
├── smart_gym_assistant.py
├── workout_trainer.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── 01_main_dashboard.png
│   ├── 02_diet_coach_habit_tracker.png
│   ├── 03_gym_buddy_performance.png
│   └── 04_smart_gym_recommender.png
│
└── AI_Gym_Fitness_Assistant_Final_Project_Report.pdf
```

## Installation

Create and activate a Python virtual environment:

```powershell
py -3.10 -m venv venv
```

Activate it:

```powershell
venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

## Run the Main Application

Start the Streamlit fitness assistant:

```powershell
streamlit run app.py
```

The main dashboard will open in the browser.

## Run the FastAPI Backend

Start the backend:

```powershell
uvicorn api:app --reload
```

FastAPI API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

The health endpoint is:

```text
http://127.0.0.1:8000/health
```

## Run the Admin Dashboard

Open another PowerShell terminal, activate the virtual environment, and run:

```powershell
streamlit run admin_dashboard.py --server.port 8502
```

The Admin Dashboard provides analytics and system monitoring.

## Testing

The following components were tested:

- AI Gym Trainer webcam and squat detection
- AI Diet Coach
- Fitness Habit Tracker
- Virtual Gym Buddy
- Performance Analyzer
- Gym Recommender & Planner
- Smart Gym Assistant
- FastAPI backend
- FastAPI health and diet endpoints
- Admin Dashboard

The FastAPI backend was also tested using its interactive Swagger documentation.

## Project Deliverables

1. Fully functional AI-based Gym & Fitness Assistant system
2. Modular fitness AI components for workout detection, diet recommendation, and habit/behavior analysis
3. FastAPI backend APIs and integration layer
4. Project documentation, report, screenshots, and testing
5. Local deployment with Admin Dashboard and analytics

## Project Limitations

This project is an academic prototype/MVP rather than a production fitness platform.

- Smart Gym equipment availability is simulated rather than connected to live IoT devices.
- Virtual Gym Buddy uses rule-based responses rather than an LLM.
- The current habit and recommendation components primarily use Python/rule-based logic rather than trained predictive ML models.
- No persistent database or cloud storage is currently implemented.
- Admin Dashboard currently uses demonstration/sample data.
- The current deployment is local rather than a cloud production deployment.
- Diet and calorie outputs are general guidance and are not medical advice.

## Future Scope

Future improvements can include:

- Advanced trained ML models
- LLM-powered fitness assistant
- Real IoT equipment integration using MQTT
- Persistent database and user accounts
- Cloud deployment
- Advanced workout and pose analysis
- Personalized long-term fitness analytics
- Production-grade frontend and backend architecture

## GitHub Repository

AI Gym & Fitness Assistant:

https://github.com/adityakumarlenka15-byte/AI-Gym-Fitness-Assistant