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

'''import byte
import socket

host = '10.0.4.194'
port = 34000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
for i in range(10):
    message = bytes('some message', 'utf-8')
    s.send(message)
s.close()
'''