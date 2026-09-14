import { useEffect, useState } from "react";

import "./App.css";

import {
  getHealth,
  getDietRecommendation,
  getHabitAnalysis,
  getGymRecommendation,
  getSmartGym,
  startTrainer,
  sendGymBuddyMessage,
  getPerformanceAnalysis,
  getPyTorchFitnessPrediction,
} from "./api";

function App() {
  const [activeModule, setActiveModule] = useState("Dashboard");

  const [backendStatus, setBackendStatus] = useState("Checking...");

  useEffect(() => {
    getHealth()
      .then(() => setBackendStatus("Backend Connected"))
      .catch(() => setBackendStatus("Backend Offline"));
  }, []);

  const modules = [
  "Dashboard",
  "AI Gym Trainer",
  "AI Dietician",
  "Habit Tracker",
  "Gym Buddy",
  "Performance",
  "Gym Planner",
  "Smart Gym",
  "PyTorch Fitness AI",
];

  return (
    <div className="app">
      {/* SIDEBAR */}
      <aside className="sidebar">
        <div className="logo">
          <div className="logo-icon">💪</div>

          <div>
            <h2>AI Gym</h2>
            <span>Fitness Assistant</span>
          </div>
        </div>

        <nav>
          {modules.map((module) => (
            <button
              key={module}
              className={
                activeModule === module
                  ? "nav-item active"
                  : "nav-item"
              }
              onClick={() => setActiveModule(module)}
            >
              {module === "Dashboard" && "🏠"}
              {module === "AI Gym Trainer" && "🏋️"}
              {module === "AI Dietician" && "🥗"}
              {module === "Habit Tracker" && "📅"}
              {module === "Gym Buddy" && "🤝"}
              {module === "Performance" && "📊"}
              {module === "Gym Planner" && "🗓️"}
              {module === "Smart Gym" && "📡"}
              {module === "PyTorch Fitness AI" && "🧠"}

              <span>{module}</span>
            </button>
          ))}
        </nav>

        <div className="sidebar-bottom">
          <div className="status">
            <span className="status-dot"></span>
            {backendStatus}
          </div>
        </div>
      </aside>

      {/* MAIN CONTENT */}
      <main className="main">
        {/* TOP BAR */}
        <header className="topbar">
          <div>
            <p className="welcome">WELCOME BACK</p>

            <h1>AI Gym & Fitness Assistant</h1>

            <p className="subtitle">
              Your intelligent fitness ecosystem for smarter workouts,
              nutrition and progress.
            </p>
          </div>

          <div className="profile">
            <div className="profile-icon">👤</div>

            <div>
              <strong>Demo User</strong>
              <small>Fitness Member</small>
            </div>
          </div>
        </header>

        {/* DASHBOARD */}
        {activeModule === "Dashboard" ? (
          <>
            {/* HERO */}
            <section className="hero">
              <div>
                <span className="badge">
                  🤖 AI POWERED FITNESS
                </span>

                <h2>
                  Train smarter.
                  <br />
                  Live healthier.
                </h2>

                <p>
                  Track your workouts, nutrition, habits and performance
                  with one intelligent fitness assistant.
                </p>

                <button
                  className="primary-btn"
                  onClick={() =>
                    setActiveModule("AI Gym Trainer")
                  }
                >
                  Start AI Workout →
                </button>
              </div>

              <div className="hero-icon">🏃</div>
            </section>

            {/* STATS */}
            <section className="stats">
              <div className="stat-card">
                <div className="stat-icon">🔥</div>

                <div>
                  <span>Current Goal</span>
                  <strong>Muscle Gain</strong>
                </div>
              </div>

              <div className="stat-card">
                <div className="stat-icon">📈</div>

                <div>
                  <span>Performance</span>
                  <strong>85.5%</strong>
                </div>
              </div>

              <div className="stat-card">
                <div className="stat-icon">✅</div>

                <div>
                  <span>Consistency</span>
                  <strong>71.4%</strong>
                </div>
              </div>

              <div className="stat-card">
                <div className="stat-icon">❤️</div>

                <div>
                  <span>Fitness Status</span>
                  <strong>Good</strong>
                </div>
              </div>
            </section>

            {/* MODULES */}
            <section className="section">
              <div className="section-title">
                <div>
                  <p className="eyebrow">AI ECOSYSTEM</p>
                  <h2>Fitness modules</h2>
                </div>

                <span>8 AI-powered tools</span>
              </div>

              <div className="module-grid">
                <ModuleCard
                  icon="🏋️"
                  title="AI Gym Trainer"
                  text="Detect exercises, count reps and provide form feedback."
                  onClick={() =>
                    setActiveModule("AI Gym Trainer")
                  }
                />

                <ModuleCard
                  icon="🥗"
                  title="AI Dietician"
                  text="Get calorie guidance and personalized meal suggestions."
                  onClick={() =>
                    setActiveModule("AI Dietician")
                  }
                />

                <ModuleCard
                  icon="📅"
                  title="Habit Tracker"
                  text="Monitor workout consistency and analyze your fitness habits."
                  onClick={() =>
                    setActiveModule("Habit Tracker")
                  }
                />

                <ModuleCard
                  icon="🤝"
                  title="Virtual Gym Buddy"
                  text="Get motivation, advice and conversational fitness support."
                  onClick={() =>
                    setActiveModule("Gym Buddy")
                  }
                />

                <ModuleCard
                  icon="📊"
                  title="Performance Analyzer"
                  text="Analyze form, rep quality and overall performance."
                  onClick={() =>
                    setActiveModule("Performance")
                  }
                />

                <ModuleCard
                  icon="🗓️"
                  title="Gym Planner"
                  text="Create weekly workout plans based on your fitness goal."
                  onClick={() =>
                    setActiveModule("Gym Planner")
                  }
                />

                <ModuleCard
                  icon="📡"
                  title="Smart Gym Assistant"
                  text="Monitor simulated IoT equipment and workout intensity."
                  onClick={() =>
                    setActiveModule("Smart Gym")
                  }
                />

                <ModuleCard
                  icon="🧠"
                  title="AI Fitness Insights"
                  text="Combine fitness data to understand your progress."
                  onClick={() =>
                    setActiveModule("Performance")
                  }
                />
              </div>
            </section>
          </>
        ) : (
          <ModulePage module={activeModule} />
        )}
      </main>
    </div>
  );
}


/* =========================================================
   MODULE CARD
========================================================= */

function ModuleCard({ icon, title, text, onClick }) {
  return (
    <button
      className="module-card"
      onClick={onClick}
    >
      <div className="module-icon">
        {icon}
      </div>

      <div className="module-content">
        <h3>{title}</h3>

        <p>{text}</p>

        <span>
          Open module →
        </span>
      </div>
    </button>
  );
}


/* =========================================================
   MODULE PAGE
========================================================= */

function ModulePage({ module }) {

  /*
    IMPORTANT:
    ALL useState hooks are placed here before any
    conditional return.

    This prevents the blank-page React Hooks error.
  */

  /* ---------------- DIETICIAN STATES ---------------- */

  const [weight, setWeight] = useState(65);
  const [height, setHeight] = useState(170);
  const [age, setAge] = useState(21);
  const [goal, setGoal] = useState("Muscle Gain");

  const [dietResult, setDietResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  /* ---------------- HABIT TRACKER STATES ---------------- */

  const [workoutDays, setWorkoutDays] = useState(5);
  const [missedDays, setMissedDays] = useState(2);

  const [habitResult, setHabitResult] = useState(null);
  const [habitLoading, setHabitLoading] = useState(false);
  const [habitError, setHabitError] = useState("");


  /* ---------------- GYM PLANNER STATES ---------------- */

  const [plannerGoal, setPlannerGoal] =
    useState("Muscle Building");

  const [plannerExperience, setPlannerExperience] =
    useState("Beginner");

  const [plannerResult, setPlannerResult] =
    useState(null);

  const [plannerLoading, setPlannerLoading] =
    useState(false);

  const [plannerError, setPlannerError] =
    useState("");


  /* ---------------- AI GYM TRAINER STATES ---------------- */
  const [trainerLoading, setTrainerLoading] = useState(false);
  const [trainerMessage, setTrainerMessage] = useState("");
  const [buddyMessage, setBuddyMessage] = useState("");

  const [buddyMessages, setBuddyMessages] = useState([
    {
      sender: "buddy",
      text: "Hey! 👋 I'm your Virtual Gym Buddy. How can I help you today?"
    }
  ]);

  const [buddyLoading, setBuddyLoading] = useState(false);
  const [buddyError, setBuddyError] = useState("");

  const [formScore, setFormScore] = useState(85);
  const [repQuality, setRepQuality] = useState(90);
  const [consistency, setConsistency] = useState(80);

  const [performanceResult, setPerformanceResult] = useState(null);
  const [performanceLoading, setPerformanceLoading] = useState(false);
  const [performanceError, setPerformanceError] = useState("");

  const [smartGymGoal, setSmartGymGoal] = useState("Muscle Gain");
  const [smartGymExperience, setSmartGymExperience] = useState("Beginner");

  const [smartGymResult, setSmartGymResult] = useState(null);
  const [smartGymLoading, setSmartGymLoading] = useState(false);
  const [smartGymError, setSmartGymError] = useState("");

  /* ---------------- PYTORCH FITNESS PREDICTION STATES ---------------- */

const [pytorchDuration, setPytorchDuration] = useState(35);
const [pytorchWorkoutDays, setPytorchWorkoutDays] = useState(5);
const [pytorchFitnessScore, setPytorchFitnessScore] = useState(72);

const [pytorchResult, setPytorchResult] = useState(null);
const [pytorchLoading, setPytorchLoading] = useState(false);
const [pytorchError, setPytorchError] = useState("");


  /* =========================================================
     DIET API
  ========================================================= */

  async function calculateDiet() {
    setLoading(true);
    setError("");
    setDietResult(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/diet",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            weight: Number(weight),
            height: Number(height),
            age: Number(age),
            goal: goal,
          }),
        }
      );

      if (!response.ok) {
        throw new Error(
          "Unable to get diet recommendation"
        );
      }

      const data = await response.json();

      setDietResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  async function openTrainer() {
  setTrainerLoading(true);
  setTrainerMessage("");

  try {
    const result = await startTrainer();
    setTrainerMessage(result.message);
  } catch (error) {
    setTrainerMessage("Could not start AI Gym Trainer.");
  } finally {
    setTrainerLoading(false);
  }
}

  /* =========================================================
     HABIT API
  ========================================================= */

  async function calculateHabit() {
    setHabitLoading(true);
    setHabitError("");
    setHabitResult(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/habit",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            workout_days: Number(workoutDays),
            missed_days: Number(missedDays),
          }),
        }
      );

      if (!response.ok) {
        throw new Error(
          "Unable to get habit analysis"
        );
      }

      const data = await response.json();

      setHabitResult(data);
    } catch (err) {
      setHabitError(err.message);
    } finally {
      setHabitLoading(false);
    }
  }

  async function sendBuddyMessage() {
  const text = buddyMessage.trim();

  if (!text || buddyLoading) {
    return;
  }

  setBuddyMessages((previous) => [
    ...previous,
    {
      sender: "user",
      text: text
    }
  ]);

  setBuddyMessage("");
  setBuddyLoading(true);
  setBuddyError("");

  try {
    const data = await sendGymBuddyMessage(text);

    setBuddyMessages((previous) => [
      ...previous,
      {
        sender: "buddy",
        text: data.response
      }
    ]);
  } catch (error) {
    setBuddyError("Could not connect to Gym Buddy.");
  } finally {
    setBuddyLoading(false);
  }
}


  /* =========================================================
     GYM PLANNER API
  ========================================================= */

  async function createGymPlan() {
    setPlannerLoading(true);
    setPlannerError("");
    setPlannerResult(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/gym-recommendation",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            goal: plannerGoal,
            experience: plannerExperience,
          }),
        }
      );

      if (!response.ok) {
        throw new Error(
          "Unable to create gym plan"
        );
      }

      const data = await response.json();

      setPlannerResult(data);
    } catch (err) {
      setPlannerError(err.message);
    } finally {
      setPlannerLoading(false);
    }
  }

  async function calculatePerformance() {
  setPerformanceLoading(true);
  setPerformanceError("");

  try {
    const data = await getPerformanceAnalysis({
      form_score: Number(formScore),
      rep_quality: Number(repQuality),
      consistency: Number(consistency),
    });

    setPerformanceResult(data);
  } catch (error) {
    setPerformanceError(
      "Could not connect to Performance Analyzer."
    );
  } finally {
    setPerformanceLoading(false);
  }
}

async function calculateSmartGym() {
  setSmartGymLoading(true);
  setSmartGymError("");

  try {
    const data = await getSmartGym({
      goal: smartGymGoal,
      experience: smartGymExperience,
    });

    setSmartGymResult(data);
  } catch (error) {
    setSmartGymError(
      "Could not connect to Smart Gym Assistant."
    );
  } finally {
    setSmartGymLoading(false);
  }
}

async function calculatePyTorchFitness() {
  setPytorchLoading(true);
  setPytorchError("");
  setPytorchResult(null);

  try {
    const data = await getPyTorchFitnessPrediction({
      workout_duration: Number(pytorchDuration),
      workout_days: Number(pytorchWorkoutDays),
      fitness_score: Number(pytorchFitnessScore),
    });

    setPytorchResult(data);
  } catch (error) {
    setPytorchError(
      "Could not connect to PyTorch Fitness Predictor."
    );
  } finally {
    setPytorchLoading(false);
  }
}


  /* =========================================================
     HABIT TRACKER PAGE
  ========================================================= */

  if (module === "Habit Tracker") {
    return (
      <section className="module-page">

        <div className="module-page-icon">
          📅
        </div>

        <p className="eyebrow">
          AI FITNESS MODULE
        </p>

        <h2>
          Habit Tracker
        </h2>

        <div className="diet-layout">

          {/* FORM */}
          <div className="coming-card">

            <h3>
              Workout Activity
            </h3>

            <p>
              Enter your recent workout activity to
              analyze your fitness consistency.
            </p>

            <label>
              Workout Days
            </label>

            <input
              type="number"
              min="0"
              value={workoutDays}
              onChange={(e) =>
                setWorkoutDays(e.target.value)
              }
            />

            <label>
              Missed Days
            </label>

            <input
              type="number"
              min="0"
              value={missedDays}
              onChange={(e) =>
                setMissedDays(e.target.value)
              }
            />

            <button
              className="primary-btn diet-btn"
              onClick={calculateHabit}
              disabled={habitLoading}
            >
              {habitLoading
                ? "Analyzing..."
                : "Analyze My Habits →"}
            </button>

            {habitError && (
              <div className="error-message">
                {habitError}
              </div>
            )}

          </div>


          {/* RESULTS */}
          {habitResult && (
            <div className="coming-card result-card">

              <p className="eyebrow">
                AI HABIT ANALYSIS
              </p>

              <h3>
                Your Fitness Consistency
              </h3>

              <div className="result-stats">

                <div>
                  <span>
                    Workout Days
                  </span>

                  <strong>
                    {habitResult["Workout Days"]}
                  </strong>
                </div>

                <div>
                  <span>
                    Missed Days
                  </span>

                  <strong>
                    {habitResult["Missed Days"]}
                  </strong>
                </div>

              </div>

              <div className="result-stats">

                <div>
                  <span>
                    Consistency
                  </span>

                  <strong>
                    {habitResult.Consistency}%
                  </strong>
                </div>

                <div>
                  <span>
                    Status
                  </span>

                  <strong>
                    {habitResult.Status}
                  </strong>
                </div>

              </div>

            </div>
          )}

        </div>

      </section>
    );
  }

  if (module === "Gym Buddy") {
  return (
    <div className="module-page">

      <div className="module-header">
        <div>
          <span className="eyebrow">AI FITNESS MODULE</span>

          <h2>Virtual Gym Buddy</h2>

          <p>
            Your virtual fitness companion for motivation,
            workout guidance and fitness tips.
          </p>
        </div>
      </div>

      <div className="coming-card buddy-card">

        <div className="buddy-title">
          <div className="coming-icon">🤝</div>

          <div>
            <h3>Chat with Gym Buddy</h3>
            <p>
              Ask about workouts, motivation, training or fitness tips.
            </p>
          </div>
        </div>

        <div className="chat-box">

          {buddyMessages.map((message, index) => (
            <div
              key={index}
              className={
                message.sender === "user"
                  ? "chat-message user-message"
                  : "chat-message buddy-message"
              }
            >
              <span>
                {message.sender === "user" ? "You" : "Gym Buddy"}
              </span>

              <p>{message.text}</p>
            </div>
          ))}

          {buddyLoading && (
            <div className="chat-message buddy-message">
              <span>Gym Buddy</span>
              <p>Thinking... 💭</p>
            </div>
          )}

        </div>

        <div className="chat-input-row">

          <input
            type="text"
            value={buddyMessage}
            onChange={(event) =>
              setBuddyMessage(event.target.value)
            }
            onKeyDown={(event) => {
              if (event.key === "Enter") {
                sendBuddyMessage();
              }
            }}
            placeholder="Type your fitness message..."
          />

          <button
            className="primary-btn"
            onClick={sendBuddyMessage}
            disabled={buddyLoading}
          >
            {buddyLoading ? "Sending..." : "Send"}
          </button>

        </div>

        {buddyError && (
          <p className="error-message">
            {buddyError}
          </p>
        )}

      </div>

    </div>
  );
}

  if (module === "AI Gym Trainer") {
  return (
    <div className="module-page">
      <div className="module-header">
        <div>
          <span className="eyebrow">Computer Vision</span>
          <h2>AI Gym Trainer</h2>
          <p>
            Real-time squat detection, repetition counting and posture
            feedback using OpenCV and MediaPipe.
          </p>
        </div>
      </div>

      <div className="coming-card">
        <div className="coming-icon">🏋️</div>

        <h3>AI Workout Trainer</h3>

        <p>
          Start the AI Gym Trainer to open your webcam and receive
          real-time workout feedback.
        </p>

        <button
          className="primary-btn"
          onClick={openTrainer}
          disabled={trainerLoading}
        >
          {trainerLoading
            ? "Starting Trainer..."
            : "🎥 Open AI Gym Trainer"}
        </button>

        {trainerMessage && (
          <p className="success-message">
            {trainerMessage}
          </p>
        )}
      </div>
    </div>
  );
}


  /* =========================================================
     GYM PLANNER PAGE
  ========================================================= */

  if (module === "Gym Planner") {
    return (
      <section className="module-page">

        <div className="module-page-icon">
          🗓️
        </div>

        <p className="eyebrow">
          AI FITNESS MODULE
        </p>

        <h2>
          Gym Planner
        </h2>

        <div className="diet-layout">

          {/* PLANNER FORM */}
          <div className="coming-card">

            <h3>
              Workout Planner
            </h3>

            <p>
              Select your fitness goal and experience level
              to generate a weekly workout plan.
            </p>

            <label>
              Fitness Goal
            </label>

            <select
              value={plannerGoal}
              onChange={(e) =>
                setPlannerGoal(e.target.value)
              }
            >
              <option value="Weight Loss">
                Weight Loss
              </option>

              <option value="Muscle Building">
                Muscle Gain
              </option>

              <option value="General Fitness">
                General Fitness
              </option>
            </select>


            <label>
              Experience Level
            </label>

            <select
              value={plannerExperience}
              onChange={(e) =>
                setPlannerExperience(e.target.value)
              }
            >
              <option value="Beginner">
                Beginner
              </option>

              <option value="Intermediate">
                Intermediate
              </option>

              <option value="Advanced">
                Advanced
              </option>
            </select>


            <button
              className="primary-btn diet-btn"
              onClick={createGymPlan}
              disabled={plannerLoading}
            >
              {plannerLoading
                ? "Creating Plan..."
                : "Create Weekly Plan →"}
            </button>


            {plannerError && (
              <div className="error-message">
                {plannerError}
              </div>
            )}

          </div>


          {/* PLANNER RESULTS */}
          {plannerResult && (
            <div className="coming-card result-card">

              <p className="eyebrow">
                AI WORKOUT PLAN
              </p>

              <h3>
                Recommended Gym Programs
              </h3>


              {Array.isArray(
                plannerResult.recommendations
              ) &&
                plannerResult.recommendations.map(
                  (recommendation, index) => (
                    <div
                      className="meal"
                      key={index}
                    >
                      <strong>
                        {recommendation}
                      </strong>
                    </div>
                  )
                )}


              <h4>
                Weekly Workout Plan
              </h4>


              {plannerResult.weekly_plan &&
                Object.entries(
                  plannerResult.weekly_plan
                ).map(
                  ([day, workout]) => (
                    <div
                      className="meal"
                      key={day}
                    >
                      <strong>
                        {day}
                      </strong>

                      <p>
                        {workout}
                      </p>
                    </div>
                  )
                )}

            </div>
          )}

        </div>

      </section>
    );
  }

  if (module === "Performance") {
  return (
    <div className="module-page">

      <div className="module-header">
        <div>
          <span className="eyebrow">AI PERFORMANCE ANALYSIS</span>

          <h2>Pose-to-Performance Analyzer</h2>

          <p>
            Analyze exercise form, repetition quality and workout
            consistency to generate an overall performance score.
          </p>
        </div>
      </div>

      <div className="diet-layout">

        <div className="coming-card">

          <div className="coming-icon">📊</div>

          <h3>Performance Metrics</h3>

          <p>
            Enter your exercise performance values.
          </p>

          <label>Form Score: {formScore}</label>

          <input
            type="range"
            min="0"
            max="100"
            value={formScore}
            onChange={(event) =>
              setFormScore(event.target.value)
            }
          />

          <label>Rep Quality: {repQuality}</label>

          <input
            type="range"
            min="0"
            max="100"
            value={repQuality}
            onChange={(event) =>
              setRepQuality(event.target.value)
            }
          />

          <label>Consistency: {consistency}</label>

          <input
            type="range"
            min="0"
            max="100"
            value={consistency}
            onChange={(event) =>
              setConsistency(event.target.value)
            }
          />

          <button
            className="primary-btn diet-btn"
            onClick={calculatePerformance}
            disabled={performanceLoading}
          >
            {performanceLoading
              ? "Analyzing..."
              : "📊 Analyze Performance"}
          </button>

          {performanceError && (
            <p className="error-message">
              {performanceError}
            </p>
          )}

        </div>

        <div className="coming-card result-card">

          <div className="coming-icon">🏆</div>

          <h3>Performance Report</h3>

          {!performanceResult ? (
            <p>
              Your performance report will appear here after
              analysis.
            </p>
          ) : (
            <>
              <div className="result-stats">

                <div>
                  <span>Performance Score</span>
                  <strong>
                    {performanceResult["Performance Score"]}
                  </strong>
                </div>

                <div>
                  <span>Performance Level</span>
                  <strong>
                    {performanceResult["Performance Level"]}
                  </strong>
                </div>

              </div>

              <h4>Feedback</h4>

              {performanceResult.Feedback.map(
                (feedback, index) => (
                  <div className="meal" key={index}>
                    💡 {feedback}
                  </div>
                )
              )}
            </>
          )}

        </div>

      </div>

    </div>
  );
}

  /* =========================================================
   PYTORCH FITNESS AI PAGE
========================================================= */

if (module === "PyTorch Fitness AI") {
  return (
    <div className="module-page">

      <div className="module-header">
        <div>
          <span className="eyebrow">
            PYTORCH NEURAL NETWORK
          </span>

          <h2>PyTorch Fitness AI</h2>

          <p>
            Predict your fitness level using a
            PyTorch neural-network model.
          </p>
        </div>
      </div>

      <div className="diet-layout">

        {/* INPUT FORM */}

        <div className="coming-card">

          <div className="coming-icon">🧠</div>

          <h3>Fitness Prediction</h3>

          <p>
            Enter your workout information to predict
            your current fitness level.
          </p>

          <label>
            Workout Duration (minutes)
          </label>

          <input
            type="number"
            min="1"
            value={pytorchDuration}
            onChange={(event) =>
              setPytorchDuration(event.target.value)
            }
          />

          <label>
            Workout Days per Week
          </label>

          <input
            type="number"
            min="0"
            max="7"
            value={pytorchWorkoutDays}
            onChange={(event) =>
              setPytorchWorkoutDays(event.target.value)
            }
          />

          <label>
            Fitness Score
          </label>

          <input
            type="number"
            min="0"
            max="100"
            value={pytorchFitnessScore}
            onChange={(event) =>
              setPytorchFitnessScore(event.target.value)
            }
          />

          <button
            className="primary-btn diet-btn"
            onClick={calculatePyTorchFitness}
            disabled={pytorchLoading}
          >
            {pytorchLoading
              ? "Predicting..."
              : "🧠 Predict Fitness Level"}
          </button>

          {pytorchError && (
            <p className="error-message">
              {pytorchError}
            </p>
          )}

        </div>


        {/* RESULT */}

        <div className="coming-card result-card">

          <div className="coming-icon">🏆</div>

          <h3>PyTorch Prediction</h3>

          {!pytorchResult ? (
            <p>
              Your predicted fitness level will appear
              here after analysis.
            </p>
          ) : (
            <>
              <div className="result-stats">

                <div>
                  <span>
                    Predicted Level
                  </span>

                  <strong>
                    {pytorchResult[
                      "Predicted Fitness Level"
                    ]}
                  </strong>
                </div>

                <div>
                  <span>
                    AI Model
                  </span>

                  <strong>
                    PyTorch
                  </strong>
                </div>

              </div>

              <div className="meal">
                <strong>Model Type</strong>

                <p>
                  Neural Network
                </p>
              </div>

              <div className="meal">
                <strong>Input Data</strong>

                <p>
                  {pytorchDuration} min workout ·{" "}
                  {pytorchWorkoutDays} days/week ·{" "}
                  {pytorchFitnessScore} fitness score
                </p>
              </div>

              <p className="disclaimer">
                This prediction is a demonstration
                generated by a small project-trained
                PyTorch model and should not be treated
                as a medical or professional fitness
                assessment.
              </p>
            </>
          )}

        </div>

      </div>

    </div>
  );
}

  /* =========================================================
     AI DIETICIAN PAGE
  ========================================================= */

  if (module === "AI Dietician") {
    return (
      <section className="module-page">

        <div className="module-page-icon">
          🥗
        </div>

        <p className="eyebrow">
          AI FITNESS MODULE
        </p>

        <h2>
          AI Dietician
        </h2>

        <div className="diet-layout">

          {/* FORM */}
          <div className="coming-card">

            <h3>
              Nutrition Profile
            </h3>

            <p>
              Enter your basic fitness information to receive
              nutrition guidance from the AI Dietician.
            </p>

            <label>
              Weight (kg)
            </label>

            <input
              type="number"
              value={weight}
              onChange={(e) =>
                setWeight(e.target.value)
              }
            />

            <label>
              Height (cm)
            </label>

            <input
              type="number"
              value={height}
              onChange={(e) =>
                setHeight(e.target.value)
              }
            />

            <label>
              Age
            </label>

            <input
              type="number"
              value={age}
              onChange={(e) =>
                setAge(e.target.value)
              }
            />

            <label>
              Fitness Goal
            </label>

            <select
              value={goal}
              onChange={(e) =>
                setGoal(e.target.value)
              }
            >
              <option value="Weight Loss">
                Weight Loss
              </option>

              <option value="Muscle Gain">
                Muscle Gain
              </option>

              <option value="Maintain Weight">
                Maintain Weight
              </option>
            </select>


            <button
              className="primary-btn diet-btn"
              onClick={calculateDiet}
              disabled={loading}
            >
              {loading
                ? "Calculating..."
                : "Get AI Nutrition Plan →"}
            </button>


            {error && (
              <div className="error-message">
                {error}
              </div>
            )}

          </div>


          {/* RESULTS */}
          {dietResult && (
            <div className="coming-card result-card">

              <p className="eyebrow">
                AI RECOMMENDATION
              </p>

              <h3>
                Your Nutrition Results
              </h3>


              <div className="result-stats">

                <div>
                  <span>
                    BMI
                  </span>

                  <strong>
                    {dietResult.BMI}
                  </strong>
                </div>


                <div>
                  <span>
                    Daily Calories
                  </span>

                  <strong>
                    {dietResult["Daily Calorie Suggestion"]}
                  </strong>
                </div>

              </div>


              <h4>
                Meal Suggestions
              </h4>


              {dietResult.Meals &&
                Object.entries(
                  dietResult.Meals
                ).map(
                  ([meal, suggestion]) => (
                    <div
                      className="meal"
                      key={meal}
                    >
                      <strong>
                        {meal}
                      </strong>

                      <p>
                        {suggestion}
                      </p>
                    </div>
                  )
                )}


              <p className="disclaimer">
                This is a general AI-generated fitness
                suggestion and is not medical advice.
              </p>

            </div>
          )}

        </div>

      </section>
    );
  }
  
  if (module === "Smart Gym") {
  return (
    <div className="module-page">

      <div className="module-header">
        <div>
          <span className="eyebrow">AI + IoT FITNESS</span>

          <h2>Smart Gym Assistant</h2>

          <p>
            Monitor simulated gym equipment data and receive
            intelligent workout recommendations.
          </p>
        </div>
      </div>

      <div className="diet-layout">

        <div className="coming-card">

          <div className="coming-icon">🏋️</div>

          <h3>Workout Settings</h3>

          <p>
            Select your fitness goal and experience level.
          </p>

          <label>Fitness Goal</label>

          <select
            value={smartGymGoal}
            onChange={(event) =>
              setSmartGymGoal(event.target.value)
            }
          >
            <option value="Muscle Gain">Muscle Gain</option>
            <option value="Weight Loss">Weight Loss</option>
            <option value="Improve Endurance">
              Improve Endurance
            </option>
            <option value="General Fitness">
              General Fitness
            </option>
          </select>

          <label>Experience Level</label>

          <select
            value={smartGymExperience}
            onChange={(event) =>
              setSmartGymExperience(event.target.value)
            }
          >
            <option value="Beginner">Beginner</option>
            <option value="Intermediate">
              Intermediate
            </option>
            <option value="Advanced">Advanced</option>
          </select>

          <button
            className="primary-btn diet-btn"
            onClick={calculateSmartGym}
            disabled={smartGymLoading}
          >
            {smartGymLoading
              ? "Reading Sensors..."
              : "🔌 Analyze Smart Gym"}
          </button>

          {smartGymError && (
            <p className="error-message">
              {smartGymError}
            </p>
          )}

        </div>

        <div className="coming-card result-card">

          <div className="coming-icon">📡</div>

          <h3>Smart Gym Report</h3>

          {!smartGymResult ? (
            <p>
              Start the analysis to receive equipment and
              sensor recommendations.
            </p>
          ) : (
            <>
              <h4>Workout Settings</h4>

              <div className="result-stats">

                <div>
                  <span>Intensity</span>
                  <strong>
                    {smartGymResult.Settings?.[
                      "Workout Intensity"
                    ]}
                  </strong>
                </div>

                <div>
                  <span>Resistance</span>
                  <strong>
                    {smartGymResult.Settings?.[
                      "Recommended Resistance"
                    ]}
                  </strong>
                </div>

              </div>

              <div className="result-stats">

                <div>
                  <span>Rest Time</span>
                  <strong>
                    {smartGymResult.Settings?.[
                      "Rest Time"
                    ]} sec
                  </strong>
                </div>

                <div>
                  <span>Equipment</span>
                  <strong>
                    {Object.keys(
                      smartGymResult.Equipment || {}
                    ).length}
                  </strong>
                </div>

              </div>

              <h4>Live Sensor Data</h4>

              <div className="meal">
                <strong>Status</strong>
                <p>
                  {smartGymResult[
                    "Live Sensor Data"
                  ]?.["Live Status"]}
                </p>
              </div>

              <div className="meal">
                <strong>Equipment</strong>
                <p>
                  {smartGymResult[
                    "Live Sensor Data"
                  ]?.Equipment || "Waiting for sensor data"}
                </p>
              </div>

              <div className="meal">
                <strong>Heart Rate</strong>
                <p>
                  {smartGymResult[
                    "Live Sensor Data"
                  ]?.["Heart Rate"] || 0}{" "}
                  BPM
                </p>
              </div>

              <div className="meal">
                <strong>Resistance</strong>
                <p>
                  {smartGymResult[
                    "Live Sensor Data"
                  ]?.Resistance || 0}
                </p>
              </div>

              <div className="meal">
                <strong>Sensor Intensity</strong>
                <p>
                  {smartGymResult[
                    "Live Sensor Data"
                  ]?.["Sensor Intensity"] || "Unknown"}
                </p>
              </div>

              <div className="meal">
                <strong>AI Recommendation</strong>
                <p>
                  {smartGymResult[
                    "Live Sensor Data"
                  ]?.Recommendation}
                </p>
              </div>

            </>
          )}

        </div>

      </div>

    </div>
  );
}


  /* =========================================================
     OTHER MODULES
  ========================================================= */

  return (
    <section className="module-page">

      <div className="module-page-icon">

        {module === "AI Gym Trainer" && "🏋️"}
        {module === "Gym Buddy" && "🤝"}
        {module === "Performance" && "📊"}
        {module === "Smart Gym" && "📡"}

      </div>

      <p className="eyebrow">
        AI FITNESS MODULE
      </p>

      <h2>
        {module}
      </h2>

      <div className="coming-card">

        <h3>
          React Frontend Connected
        </h3>

        <p>
          This module interface is ready.
          We will connect it to the FastAPI backend next.
        </p>

        <div className="connection">

          <span className="status-dot"></span>

          Backend integration: Next step

        </div>

      </div>

    </section>
  );
}


export default App;