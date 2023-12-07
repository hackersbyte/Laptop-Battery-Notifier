# Laptop Battery Notifier

![Battery Notifier Logo](link/to/logo.png)

## Overview

Laptop Battery Notifier is a simple Python script (`battery.py`) that runs in the background and notifies the user when the laptop battery is fully charged or reaches a low level. The script periodically checks the battery status and sends notifications, making it a handy tool to avoid overcharging or sudden shutdowns due to low battery.

## Features

- **Battery Status Monitoring:** Continuously monitors the laptop battery status.
- **Notifications:** Sends desktop notifications when the battery is fully charged or reaches a low level.
- **Audio Alerts:** Plays audio alerts when the battery is fully charged or reaches a low level.
- **Customizable:** Easily customizable script for users to modify based on their preferences.

## Requirements

- Python 3.x
- [psutil](https://github.com/giampaolo/psutil): Cross-platform library for accessing system details.
- [plyer](https://github.com/plyer/plyer): Python library for accessing features commonly found on various platforms.
- [playsound](https://github.com/TaylorSMarks/playsound): Pure Python implementation with no dependencies for playing sound files.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/hackersbyte/laptop-battery-notifier.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python battery.py
    ```

## Usage

1. Run the script using the provided instructions in the Installation section.
2. Keep the script running in the background.
3. Receive desktop notifications and audio alerts based on the battery status.

## Customization

- **Notification Settings:** Modify notification titles and messages in the `battery.py` script for a personalized experience.
- **Audio Files:** Replace `battery_full.aac` and `battery_low.aac` with your preferred audio files.

## Contribution

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request. Please follow the [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Thank you to the creators of [psutil](https://github.com/giampaolo/psutil), [plyer](https://github.com/plyer/plyer), and [playsound](https://github.com/TaylorSMarks/playsound) for their valuable libraries.

---

**Note:** This README is a template. Please update it with accurate and relevant information specific to your project.
