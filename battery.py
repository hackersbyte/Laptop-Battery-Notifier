import psutil
import time
from plyer import notification
from playsound import playsound


def play_audio(battery_full=True):
    audio_file = "battery_full.aac" if battery_full else "battery_low.aac"
    playsound(audio_file)


while True:
    battery = psutil.sensors_batter()
    plugged = battery.power_plugged
    percent = battery.percent

    # Check battery status and notify accordingly
    if percent == 100 and plugged:
        # Notify that the laptop is fully charged
        # Use a notificaton library or play a sound here
        notification.notify(
            title="Battery Full",
            message=f"Battery fully Charged",
        )
        play_audio()
    elif percent <= 10 and not plugged:
        # Notify that the laptop needs to be recharged immediately
        # Use a notificaton library or play a sound here
        print("Laptop needs to be recharged immediately. Plug in the Charger!")
        play_audio(battery_full=False)
        
    # Sleep for a certtain interval before checking again
    time.sleep(60)

    