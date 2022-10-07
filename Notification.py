from plyer import notification
import time

while True:
    time.sleep(9)
    notification.notify(
        title = 'Suspect found in your area',
        message = 'message',
        app_icon = "Notif.ico",
        timeout = 10,
    )