from pymongo import MongoClient

# Connect to local MongoDB
MONGO_URL = "mongodb://localhost:27017/"

client = MongoClient(MONGO_URL)

# Create/select project database
db = client["ai_gym_fitness"]

# Collections
users_collection = db["users"]
workouts_collection = db["workouts"]
diet_collection = db["diet_records"]
habit_collection = db["habit_records"]
performance_collection = db["performance_records"]
iot_collection = db["iot_records"]

def test_database_connection():
    try:
        client.admin.command("ping")
        return True
    except Exception:
        return False

def save_user(user_data):
    try:
        result = users_collection.insert_one(user_data)
        return str(result.inserted_id)
    except Exception as e:
        print("Error saving user:", e)
        return None

def save_workout(workout_data):
    try:
        result = workouts_collection.insert_one(workout_data)
        return str(result.inserted_id)
    except Exception as e:
        print("Error saving workout:", e)
        return None

def save_diet_record(diet_data):
    try:
        result = diet_collection.insert_one(diet_data)
        return str(result.inserted_id)
    except Exception as e:
        print("Error saving diet record:", e)
        return None

def save_habit_record(habit_data):
    try:
        result = habit_collection.insert_one(habit_data)
        return str(result.inserted_id)
    except Exception as e:
        print("Error saving habit record:", e)
        return None

def save_performance_record(performance_data):
    try:
        result = performance_collection.insert_one(performance_data)
        return str(result.inserted_id)
    except Exception as e:
        print("Error saving performance record:", e)
        return None

def get_users():
    try:
        return list(users_collection.find())
    except Exception as e:
        print("Error retrieving users:", e)
        return []

def get_user_by_id(user_id):
    try:
        from bson.objectid import ObjectId
        return users_collection.find_one({"_id": ObjectId(user_id)})
    except Exception as e:
        print("Error retrieving user:", e)
        return None

def save_workout_for_user(user_id, workout_data):
    try:
        from bson.objectid import ObjectId
        workout_data["user_id"] = ObjectId(user_id)
        result = workouts_collection.insert_one(workout_data)
        return str(result.inserted_id)
    except Exception as e:
        print("Error saving user workout:", e)
        return None


def save_diet_for_user(user_id, diet_data):
    try:
        from bson.objectid import ObjectId
        diet_data["user_id"] = ObjectId(user_id)
        result = diet_collection.insert_one(diet_data)
        return str(result.inserted_id)
    except Exception as e:
        print("Error saving user diet:", e)
        return None


def save_habit_for_user(user_id, habit_data):
    try:
        from bson.objectid import ObjectId
        habit_data["user_id"] = ObjectId(user_id)
        result = habit_collection.insert_one(habit_data)
        return str(result.inserted_id)
    except Exception as e:
        print("Error saving user habit:", e)
        return None


def save_performance_for_user(user_id, performance_data):
    try:
        from bson.objectid import ObjectId
        performance_data["user_id"] = ObjectId(user_id)
        result = performance_collection.insert_one(performance_data)
        return str(result.inserted_id)
    except Exception as e:
        print("Error saving user performance:", e)
        return None

def save_iot_record(iot_data):
    try:
        result = iot_collection.insert_one(iot_data)
        return str(result.inserted_id)
    except Exception as e:
        print("Error saving IoT record:", e)
        return None                                