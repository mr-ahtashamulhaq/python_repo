import time  # To pause execution for some time
from plyer import notification  # To show desktop notification

# Ensure 'notification' is not overwritten anywhere in your code

while True:
    # 1. Print a message on the console
    print("Time to drink water! 💧")
    # Call notify from plyer.notification to avoid any shadowing issues
    notification.notify(
        title="💧 Hydration Reminder",
        message="It's time to drink water and stay healthy!",
        timeout=5  # Notification stays for 5 seconds
    )

    
    # 4. Wait for 30 minutes (1800 seconds) before reminding again
    time.sleep(1800)
