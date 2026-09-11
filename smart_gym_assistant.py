import json
import time
import paho.mqtt.client as mqtt

from database import save_iot_record

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
EQUIPMENT_TOPIC = "ai_gym/equipment"


def get_workout_settings(goal, experience):
    intensity = "Moderate"
    resistance = "Medium"
    rest_time = 60

    if goal == "Weight Loss":
        intensity = "High"
        resistance = "Medium"
        rest_time = 45

    elif goal == "Muscle Gain":
        intensity = "High"
        resistance = "High"
        rest_time = 90

    elif goal == "Improve Endurance":
        intensity = "Moderate"
        resistance = "Low"
        rest_time = 45

    if experience == "Beginner":
        if intensity == "High":
            intensity = "Moderate"

        if resistance == "High":
            resistance = "Medium"

    elif experience == "Advanced":
        if intensity == "Moderate":
            intensity = "High"

    return {
        "Workout Intensity": intensity,
        "Recommended Resistance": resistance,
        "Rest Time": rest_time
    }


def get_equipment_status():
    return {
        "Treadmill": "Available",
        "Exercise Bike": "Available",
        "Weight Machine": "Available",
        "Dumbbells": "Available"
    }


def get_live_equipment_data(timeout=3):
    latest_data = {"data": None}

    def on_message(client, userdata, message):
        try:
            data = json.loads(message.payload.decode())

            # Save live IoT sensor data to MongoDB
            save_iot_record(data)

            userdata["data"] = data

        except Exception:
            userdata["data"] = None

    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id="ai-gym-smart-gym-reader"
    )

    client.user_data_set(latest_data)
    client.on_message = on_message

    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.subscribe(EQUIPMENT_TOPIC)

        client.loop_start()

        start_time = time.time()

        while time.time() - start_time < timeout:
            if latest_data["data"] is not None:
                break
            time.sleep(0.1)

        client.loop_stop()
        client.disconnect()

        return latest_data["data"]

    except Exception as e:
        print("MQTT reader error:", e)
        return None


def generate_live_recommendation(sensor_data):
    if not sensor_data:
        return {
            "Live Status": "No sensor data received",
            "Recommendation": "Start the MQTT sensor simulator."
        }

    heart_rate = sensor_data.get("heart_rate", 0)
    intensity = sensor_data.get("intensity", "Unknown")
    resistance = sensor_data.get("resistance", 0)

    if heart_rate >= 140:
        recommendation = (
            "Heart rate is high. Reduce workout intensity "
            "and take a longer rest."
        )

    elif heart_rate >= 120:
        recommendation = (
            "Heart rate is elevated. Maintain moderate intensity "
            "and monitor your recovery."
        )

    else:
        recommendation = (
            "Heart rate is within the simulated target range. "
            "Continue with controlled exercise."
        )

    return {
        "Live Status": "Sensor data received",
        "Equipment": sensor_data.get("equipment", "Unknown"),
        "Heart Rate": heart_rate,
        "Resistance": resistance,
        "Sensor Intensity": intensity,
        "Recommendation": recommendation
    }


def smart_gym_assistant(goal, experience):
    settings = get_workout_settings(goal, experience)
    equipment = get_equipment_status()

    live_data = get_live_equipment_data()
    live_recommendation = generate_live_recommendation(live_data)

    return {
        "Settings": settings,
        "Equipment": equipment,
        "Live Sensor Data": live_recommendation
    }