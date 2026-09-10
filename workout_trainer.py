import cv2
import mediapipe as mp
import math
import sys


# -----------------------------------
# Calculate angle between 3 points
# -----------------------------------
def calculate_angle(a, b, c):
    angle = math.degrees(
        math.atan2(c[1] - b[1], c[0] - b[0])
        - math.atan2(a[1] - b[1], a[0] - b[0])
    )

    angle = abs(angle)

    if angle > 180:
        angle = 360 - angle

    return angle


# -----------------------------------
# AI Gym Trainer Function
# -----------------------------------
def run_workout_trainer():

    # -----------------------------------
    # MediaPipe Pose Setup
    # -----------------------------------
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    pose = mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    # -----------------------------------
    # Open Webcam
    # -----------------------------------
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        pose.close()
        return

    # -----------------------------------
    # Variables
    # -----------------------------------
    counter = 0
    stage = None
    feedback = "Stand in front of the camera"

    # -----------------------------------
    # Main Loop
    # -----------------------------------
    while True:

        success, frame = cap.read()

        if not success:
            print("Could not read webcam.")
            break

        # Flip image for mirror effect
        frame = cv2.flip(frame, 1)

        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        # Detect pose
        results = pose.process(rgb_frame)

        if results.pose_landmarks:

            landmarks = results.pose_landmarks.landmark

            # Left side body points
            shoulder = landmarks[
                mp_pose.PoseLandmark.LEFT_SHOULDER
            ]

            hip = landmarks[
                mp_pose.PoseLandmark.LEFT_HIP
            ]

            knee = landmarks[
                mp_pose.PoseLandmark.LEFT_KNEE
            ]

            ankle = landmarks[
                mp_pose.PoseLandmark.LEFT_ANKLE
            ]

            # Convert normalized coordinates
            shoulder_point = (
                int(shoulder.x * frame.shape[1]),
                int(shoulder.y * frame.shape[0])
            )

            hip_point = (
                int(hip.x * frame.shape[1]),
                int(hip.y * frame.shape[0])
            )

            knee_point = (
                int(knee.x * frame.shape[1]),
                int(knee.y * frame.shape[0])
            )

            ankle_point = (
                int(ankle.x * frame.shape[1]),
                int(ankle.y * frame.shape[0])
            )

            # Calculate knee angle
            knee_angle = calculate_angle(
                hip_point,
                knee_point,
                ankle_point
            )

            # -----------------------------------
            # Squat Detection
            # -----------------------------------

            if knee_angle < 100:

                stage = "down"

                if knee_angle < 80:
                    feedback = "Good squat depth"
                else:
                    feedback = "Go a little lower"

            elif knee_angle > 160:

                if stage == "down":
                    counter += 1

                stage = "up"
                feedback = "Good! Keep going"

            else:

                feedback = "Move smoothly"

            # -----------------------------------
            # Draw Pose
            # -----------------------------------

            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

            # -----------------------------------
            # Display Information
            # -----------------------------------

            cv2.rectangle(
                frame,
                (10, 10),
                (360, 150),
                (255, 255, 255),
                -1
            )

            cv2.putText(
                frame,
                f"Squats: {counter}",
                (25, 55),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2
            )

            cv2.putText(
                frame,
                f"Angle: {int(knee_angle)}",
                (25, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 0),
                2
            )

            cv2.putText(
                frame,
                feedback,
                (25, 125),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 0),
                2
            )

        # Show webcam window
        cv2.imshow(
            "AI Gym Trainer - Squat Detection",
            frame
        )

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # -----------------------------------
    # Release Resources
    # -----------------------------------
    cap.release()
    cv2.destroyAllWindows()
    pose.close()

    print(f"Workout completed! Total squats: {counter}")


# -----------------------------------
# Run only when file is executed
# -----------------------------------
if __name__ == "__main__":
    run_workout_trainer()