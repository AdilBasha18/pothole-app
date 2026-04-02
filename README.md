# Pothole Detection System - Setup Instructions

This is a Flask-based web application that uses a YOLOv8 model to detect potholes, classify their severity, and estimate repair urgency.

## Prerequisites

Since Python is not currently installed on your system, you will need to install it to run this application.

1.  **Install Python**: Download and install Python (version 3.9 or higher) from [python.org](https://www.python.org/downloads/).
    *   **IMPORTANT**: During installation, check the box that says **"Add Python to PATH"**.

## Installation

1.  **Open Command Prompt** (cmd) or PowerShell in this project directory:
    `c:\Users\SHAIK ADIL BASHA\Downloads\yolov8_pothole_model-20260125T163718Z-1-001` or wherever you moved it.

2.  **Install Dependencies**:
    Run the following command to install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Start the Server**:
    Run the application using Python:
    ```bash
    python app.py
    ```

2.  **Access the Website**:
    Open your web browser and go to:
    `http://127.0.0.1:5000`

## Features

-   **Home**: Project overview.
-   **Login/Signup**: Create an account to access detection features.
-   **Detection**: Upload images or videos.
    -   Validates if the image is a road scene.
    -   Detects potholes using YOLOv8.
    -   Classifies severity (Small, Medium, Large).
    -   Estimates repair urgency (Low, Medium, High).

## Project Structure

-   `app.py`: Main backend logic (Flask).
-   `requirements.txt`: List of dependencies.
-   `templates/`: HTML files for the website pages.
-   `static/`: CSS styles, uploads, and prediction results.
-   `yolov8_pothole_model/`: Contains the trained `.pt` model file.

## Troubleshooting

-   **"Python was not found"**: Make sure you installed Python and added it to your PATH.
-   **Model not found**: Ensure the `best.pt` file is located at `yolov8_pothole_model/yolov8n_pothole_detection/weights/best.pt`.
