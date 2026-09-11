import json
import time
import random
import paho.mqtt.client as mqtt


# ==========================================
# MQTT CONFIGURATION
# ==========================================

MQTT_BROKER = "localhost"
MQTT_PORT = 1883

EQUIPMENT_TOPIC = "ai_gym/equipment"


# ==========================================
# MQTT CONNECTION
# ==========================================

def create_mqtt_client():
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id="ai-gym-assistant"
    )

    return client


# ==========================================
# CONNECT TO MQTT BROKER
# ==========================================

def connect_mqtt():

    client = create_mqtt_client()

    try:
        client.connect(
            MQTT_BROKER,
            MQTT_PORT,
            60
        )

        print("MQTT connection: OK")

        return client

    except Exception as e:

        print("MQTT connection failed:", e)

        return None


# ==========================================
# EQUIPMENT SENSOR DATA
# ==========================================

def generate_equipment_data():

    data = {
        "equipment": random.choice([
            "Treadmill",
            "Exercise Bike",
            "Weight Machine",
            "Dumbbells"
        ]),
        "heart_rate": random.randint(80, 150),
        "resistance": random.randint(1, 10),
        "intensity": random.choice([
            "Low",
            "Moderate",
            "High"
        ]),
        "timestamp": time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    return data


# ==========================================
# PUBLISH SENSOR DATA
# ==========================================

def publish_equipment_data(client):

    data = generate_equipment_data()

    message = json.dumps(data)

    client.publish(
        EQUIPMENT_TOPIC,
        message
    )

    print(
        "Published:",
        message
    )


# ==========================================
# MQTT SENSOR SIMULATOR
# ==========================================

def run_iot_simulator():

    client = connect_mqtt()

    if client is None:
        return

    try:

        print(
            "Starting AI Gym IoT sensor simulator..."
        )

        while True:

            publish_equipment_data(client)

            time.sleep(5)

    except KeyboardInterrupt:

        print(
            "\nIoT simulator stopped."
        )

    finally:

        client.disconnect()


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    run_iot_simulator()