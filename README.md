# iPhone/Local to PC File Transfer Tool

A simple, lightweight Flask application designed to transfer files (photos, videos, documents) from your mobile device (iPhone, Android) or another computer to your PC over a local Wi-Fi network.

## Features

-   **Zero Configuration:** Automatically detects your PC's local IP address.
-   **No Internet Required:** Works entirely over your local Wi-Fi network (fast & private).
-   **Batch Uploading:** Select and upload multiple files at once.
-   **Real-time Progress:** Visual progress bars for individual file uploads.
-   **Organized Storage:** Automatically sorts uploaded files into daily folders (e.g., `uploads/2026-01-22/`).
-   **Duplicate Handling:** Smartly renames duplicate files to prevent overwriting.
-   **Large File Support:** Configured to handle large video files (up to 16GB).

## Prerequisites

-   Python 3.6 or higher
-   A shared Wi-Fi network (your PC and phone must be on the same network)

## Installation

1.  **Clone or Download** this repository to your computer.

2.  **Install Dependencies:**
    You only need `Flask`. You can install it via pip:
    ```bash
    pip install flask
    ```

## Usage

1.  **Start the Application:**
    Open your terminal or command prompt in the project directory and run:
    ```bash
    python app.py
    ```

2.  **Connect from your Phone:**
    The application will print the access URL in the terminal. It usually looks like:
    ```
    http://192.168.1.X:5000
    ```
    -   Open Safari (iOS) or Chrome (Android).
    -   Type the address exactly as shown in your terminal.

3.  **Transfer Files:**
    -   Tap the cloud icon or "Tap to select..." area on your phone.
    -   Select the photos or videos you want to send.
    -   The upload will start immediately.
    -   Watch the progress bars for status.

4.  **Locate Files:**
    Once finished, your files will be available on your PC in the `uploads` folder within the project directory.

## Troubleshooting

-   **Cannot connect?**
    -   Ensure both devices are on the **same Wi-Fi network**.
    -   Check if your PC's firewall is blocking port 5000. You may need to allow Python through the firewall.
    -   Try accessing the URL from the PC itself (`http://localhost:5000`) to verify the app is running.

-   **Upload fails?**
    -   Ensure you have enough disk space on your PC.
    -   Very large files might take some time; keep the browser tab open until completion.
