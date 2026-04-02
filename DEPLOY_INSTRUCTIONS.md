# Deployment Instructions

1.  **Create a Hugging Face Account**: Go to [huggingface.co](https://huggingface.co/) and sign up.
2.  **Create a New Space**:
    *   Click on your profile picture -> "New Space".
    *   Name: `roadsafe-pothole-detection` (or similar).
    *   License: `MIT` (optional).
    *   **SDK**: Select **Docker** (This is important!).
    *   Click "Create Space".
3.  **Upload Files**:
    *   In your new Space, go to the "Files" tab.
    *   Click "Add file" -> "Upload files".
    *   Drag and drop ALL the files from your folder `yolov8_pothole_model...` into the browser window.
    *   **Important**: Make sure you include:
        *   `Dockerfile`
        *   `app.py`
        *   `requirements.txt`
        *   `best.pt`
        *   `users.db`
        *   `static/` folder (and its contents)
        *   `templates/` folder (and its contents)
    *   Click "Commit changes to main".

The Space will start "Building". It might take 2-3 minutes. Once it says "Running", your app is online!
