from plyer import notification
import time

while True:
    time.sleep(2)
    notification.notify(
        title = 'Alert From Police HQ',
        message = 'Suspected person found in your area',
        app_icon = "Notif.ico",
        timeout = 20,
    )