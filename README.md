   # 🌱 WellSight AI
   
   ### AI-Powered Workspace Wellness Assistant
   
   WellSight AI is a real-time computer vision-based workspace wellness assistant designed to encourage healthier digital working habits.
   
   The system uses computer vision to monitor user presence, approximate face-to-camera distance, sitting duration and break intervals, and provides real-time wellness scores and recommendations.
   
   ---
   
   ## 🎯 Problem Statement
   
   Long periods of continuous computer usage can lead to poor workspace habits such as sitting too close to the screen and working for extended periods without taking breaks.
   
   WellSight AI aims to provide a simple, real-time monitoring system that encourages users to maintain healthier workspace habits.
   
   ---
   
   ## ✨ Features
   
   - 👤 Real-time user presence detection
   - 📏 Face-to-camera distance estimation
   - 🪑 Sitting-time monitoring
   - ⏱️ Break countdown and reminder
   - 🔔 Audio break alert
   - 📊 Real-time wellness score
   - 💡 Contextual wellness recommendations
   - 🧠 Computer vision-based monitoring
   - 📋 Excel-based session database
   
   ---
   
  ## 🧠 How It Works

```text
Webcam
   ↓
Face Detection
   ↓
Face Size Estimation
   ↓
Distance Classification
   ↓
Session & Break Monitoring
   ↓
Wellness Score
   ↓
Real-Time Recommendation

```

## 🖥️ Application Dashboard

![WellSight AI Dashboard](wellsight-dashboard.jpeg)
---

## 🚀 Getting Started

### Prerequisites

- Windows operating system
- Python 3.10
- Webcam

### 1. Clone the repository

```bash
git clone https://github.com/Jayam-Parthiban/WellSight-AI.git
cd WellSight-AI
```

### 2. Install dependencies

```bash
py -3.10 -m pip install -r requirements.txt
```
### 3. Start the application

```bash
py -3.10 database.py
```

### 4. Enter user details

The application will ask for:

- User / Candidate Name
- Reference Number

The Wellness Monitor will then launch automatically.

### 5. Use the Wellness Monitor

The system provides real-time monitoring of:

- User presence
- Face-to-camera distance
- Sitting duration
- Break intervals
- Wellness score
- Wellness recommendations

Press **Q** in the Wellness Monitor window to finish the session.

The session information is then stored in the Excel database.
---

## 📁 Project Structure

```text
WellSight-AI/
│
├── wellness_monitor.py       # Main wellness monitoring application
├── database.py               # User login and Excel session database
├── requirements.txt          # Python dependencies
├── wellsight-dashboard.jpeg  # Application dashboard screenshot
└── README.md                 # Project documentation
```

### File Overview

| File | Purpose |
|---|---|
| `wellness_monitor.py` | Runs the real-time computer vision wellness monitor |
| `database.py` | Collects user details and stores session information |
| `requirements.txt` | Contains the required Python packages |
| `wellsight-dashboard.jpeg` | Screenshot of the application dashboard |
| `README.md` | Project documentation |

---

## 🧠 System Architecture

WellSight AI follows a real-time computer vision pipeline:

```text
                    Webcam
                       │
                       ▼
                Frame Acquisition
                       │
                       ▼
              MediaPipe Face Detection
                       │
                       ▼
              Face Bounding Box
                       │
                       ▼
             Face Width Estimation
                       │
                       ▼
          Distance Classification
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Too Far       Optimal     Too Close
          │            │            │
          └────────────┼────────────┘
                       ▼
              Session Monitoring
                       │
              ┌────────┴────────┐
              ▼                 ▼
        Sitting Time       Break Timer
              │                 │
              └────────┬────────┘
                       ▼
                Wellness Score
                       │
                       ▼
          Recommendation Engine
                       │
                       ▼
                Live Dashboard
```

### Core Processing

1. **Face Detection**  
   MediaPipe detects the user's face from the webcam stream.

2. **Distance Estimation**  
   The width of the detected face bounding box is used as a proxy for the user's distance from the camera.

3. **Distance Classification**  
   The system classifies the user's position as **Too Far**, **Optimal**, or **Too Close**.

4. **Session Monitoring**  
   The application tracks how long the user remains present and maintains a break countdown.

5. **Wellness Scoring**  
   The system calculates a real-time wellness score based on distance and break conditions.

6. **Recommendation Engine**  
   Contextual recommendations are displayed according to the user's current workspace condition.

7. **Session Database**  
   User details and completed session information are stored in an Excel database using OpenPyXL.

---

## 🔮 Future Improvements

- 🧍 Advanced posture detection using pose landmarks
- 👁️ Blink and eye-strain analysis
- 🪑 More detailed ergonomic assessment
- 📈 Historical wellness analytics
- 📊 Interactive wellness reports and visualizations
- ☁️ Cloud-based session storage
- 🤖 Personalized wellness recommendations

---

## ⚠️ Limitations

- Face width is used as an approximate indicator of camera distance rather than a direct physical distance measurement.
- The current system focuses primarily on workspace distance, sitting duration and break intervals.
- Wellness scoring is an application-defined metric and should not be interpreted as a medical assessment.
- Performance depends on webcam quality, lighting conditions and face visibility.
- The current implementation is designed for Windows environments.

