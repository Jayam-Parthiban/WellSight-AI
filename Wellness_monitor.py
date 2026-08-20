import cv2
import mediapipe as mp
import time
import numpy as np
import winsound
from pathlib import Path

# -------------------------------------------------
# Session output for database.py
# -------------------------------------------------
SESSION_FILE = Path(__file__).resolve().parent / "wellness_session.txt"


cap = cv2.VideoCapture(0)

cv2.namedWindow("Wellness Monitor", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Wellness Monitor", 1600, 700)

mp_face_detection = mp.solutions.face_detection

face_detection = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)

start_time = time.time()
user_present = False
elapsed_time = 0
width = 0

break_time = 30
break_countdown = 30

wellness_score = 100
alert_played = False

distance_status = "Waiting..."
recommendation = "Waiting for user..."
health_tip = "Waiting for user..."

health_tips = [
    "Blink your eyes regularly.",
    "Keep your back straight.",
    "Drink water frequently.",
    "Keep the monitor at eye level.",
    "Take deep breaths."
]


while True:

    success, frame = cap.read()

    if not success:
        print("Couldn't read camera.")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb.flags.writeable = False

    results = face_detection.process(rgb)

    rgb.flags.writeable = True

    if results.detections:

        if not user_present:
            start_time = time.time()
            alert_played = False

        user_present = True

        elapsed_time = int(
            time.time() - start_time
        )

        break_countdown = max(
            0,
            break_time - elapsed_time
        )

        tip_index = (
            elapsed_time // 10
        ) % len(health_tips)

        health_tip = health_tips[tip_index]

        for detection in results.detections:

            bbox = (
                detection
                .location_data
                .relative_bounding_box
            )

            h, w, c = frame.shape

            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            width = int(bbox.width * w)
            height = int(bbox.height * h)

            # -----------------------------------------
            # Distance
            # -----------------------------------------
            if width > 550:
                distance_status = "Too Close"

            elif width > 300:
                distance_status = "Optimal"

            else:
                distance_status = "Too Far"

            # -----------------------------------------
            # Recommendation
            # -----------------------------------------
            if break_countdown == 0:

                recommendation = (
                    "Take a short break!"
                )

                if not alert_played:

                    winsound.Beep(
                        1000,
                        500
                    )

                    alert_played = True

            elif distance_status == "Too Close":

                recommendation = "Move away"

            elif distance_status == "Too Far":

                recommendation = "Move closer"

            else:

                recommendation = (
                    "Excellent posture!"
                )

            # -----------------------------------------
            # Wellness Score
            # -----------------------------------------
            wellness_score = 100

            if distance_status != "Optimal":
                wellness_score -= 30

            if break_countdown == 0:
                wellness_score -= 40

            if not user_present:
                wellness_score -= 30

            cv2.rectangle(
                frame,
                (x, y),
                (x + width, y + height),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Face Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    else:

        user_present = False
        health_tip = "Waiting for user..."

        cv2.putText(
            frame,
            "User Absent",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    # ---------------------------------------------
    # Dashboard
    # ---------------------------------------------
    dashboard = np.ones(
        (frame.shape[0], 500, 3),
        dtype=np.uint8
    ) * 255

    combined = np.hstack(
        (frame, dashboard)
    )

    dashboard_x = frame.shape[1] + 20

    cv2.putText(
        combined,
        "Ambient AI",
        (dashboard_x, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 0, 0),
        2
    )

    cv2.putText(
        combined,
        "Workspace Wellness Assistant",
        (dashboard_x, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 0),
        2
    )

    status = (
        "Active"
        if user_present
        else "Idle"
    )

    cv2.putText(
        combined,
        f"Status : {status}",
        (dashboard_x, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 120, 0)
        if user_present
        else (0, 0, 255),
        2
    )

    cv2.putText(
        combined,
        f"Face Width : {width} px",
        (dashboard_x, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        2
    )

    cv2.putText(
        combined,
        f"Distance: {distance_status}",
        (dashboard_x, 180),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        2
    )

    cv2.putText(
        combined,
        f"Sitting Time : {elapsed_time} sec",
        (dashboard_x, 220),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        2
    )

    cv2.putText(
        combined,
        f"Break In    : {break_countdown} sec",
        (dashboard_x, 260),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        2
    )

    # Score Color
    if wellness_score >= 80:
        score_color = (0, 180, 0)

    elif wellness_score >= 50:
        score_color = (0, 165, 255)

    else:
        score_color = (0, 0, 255)

    cv2.putText(
        combined,
        f"Wellness Score : {wellness_score}/100",
        (dashboard_x, 300),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        score_color,
        2
    )

    cv2.putText(
        combined,
        "Recommendation:",
        (dashboard_x, 350),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        2
    )

    cv2.putText(
        combined,
        recommendation,
        (dashboard_x, 380),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    cv2.putText(
        combined,
        "Health Tip:",
        (dashboard_x, 430),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        2
    )

    cv2.putText(
        combined,
        health_tip,
        (dashboard_x, 460),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 120, 0),
        2
    )

    cv2.imshow(
        "Wellness Monitor",
        combined
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):

        # Save the final dashboard values for database.py.
        SESSION_FILE.write_text(
            f"Wellness Score: {wellness_score}/100\n"
            f"Face Width: {width} px\n"
            f"Distance: {distance_status}\n"
            f"Sitting Time: {elapsed_time} sec\n"
            f"Break Countdown: {break_countdown} sec\n"
            f"Recommendation: {recommendation}\n"
            f"Health Tip: {health_tip}\n",
            encoding="utf-8"
        )

        break


cap.release()
cv2.destroyAllWindows()