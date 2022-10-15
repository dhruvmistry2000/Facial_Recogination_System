# OpenCV program to detect face in real time
# import libraries of python OpenCV
# where its functionality resides

from cv2 import cv2

import clx.xms
import requests

# By creating an account in sinch sms You can get your code.
# code for sms starts here
# client is a object that carries your unique token.
client = clx.xms.Client(service_plan_id='your_service id',
                        token='token_id')

create = clx.xms.api.MtBatchTextSmsCreate()
create.sender = 'sender no.'
create.recipients = {'recipients no.'}
create.body = 'This is a test message from your Sinch account'
# code for sms ends here
# Face Recognition starts from here.
# load the required trained XML classifiers
# https://github.com/opencv/opencv/blob/master
# /data/haarcascades/haarcascade_frontalface_default.xml
# Trained XML classifiers describes some features of some
# object we want to detect a cascade function is trained
# from a lot of positive(faces) and negative(non-faces)
# images.

detector = cv2.CascadeClassifier(
    "path")

# capture frames from a camera

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# We want to send sms only once not until the face is there and for that we are
# initializing the counter
counter = 0
# loop runs if capturing has been initialized.

while True:
    # reads frames from a camera

    ret, img = cap.read()

    if ret:
        # convert to gray scale of each frames

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detects faces of different sizes in the input image

        faces = detector.detectMultiScale(gray, 1.1, 4)

        for face in faces:

            x, y, w, h = face
            # if there is any face and counter is zero then only it will send notification to the sender
            if (face.any() and counter == 0):
                try:
                    batch = client.create_batch(create)
                except (requests.exceptions.RequestException, clx.xms.exceptions.ApiException) as ex:
                    print('Failed to communicate with XMS: %s' % str(ex))
        # sms ends here
        # To draw a rectangle in a face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Face", img)
    counter = 1
# Wait for 'q' key to stop

key = cv2.waitKey(1)
if key == ord("q"):
    break
# Close the window
cap.release()
# De-allocate any associated memory usage

cv2.destroyAllWindows()
